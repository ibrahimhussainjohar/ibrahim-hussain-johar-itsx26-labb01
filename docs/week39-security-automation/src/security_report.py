# src/security_report.py
# Säkerhetsautomatisering - ITSX26 Kursvecka 5

# ==========================================
# KONFIGURATION AV SÖKVÄGAR OCH FILER
# ==========================================
AUTH_LOG_PATH = "data/auth.log"
ACCESS_LOG_PATH = "data/access.log"
INDICATORS_PATH = "data/suspicious_ips.txt"
OUTPUT_REPORT_PATH = "output/security_report.txt"

def load_indicators(file_path):
    """Läser indikatorlistan och sparar unika IP-adresser i en mängd (set)."""
    indicators = set()
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                ip = line.strip()
                if ip:
                    indicators.add(ip)
    except FileNotFoundError:
        print(f"Kunde inte hitta {file_path}. Kontrollera projektstrukturen och kör från projektroten.")
        raise SystemExit(1)
    return indicators

def analyze_auth_log(file_path):
    """Analyserar auth.log för att räkna misslyckade inloggningar och IP-adresser."""
    failed_count = 0
    malformed_count = 0
    ip_counts = {}
    
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                if line.strip() == "":
                    continue
                parts = line.split()

                # Extrahera fält som börjar med src=
                source_fields = [p for p in parts if p.startswith("src=")]
                if not source_fields:
                    malformed_count += 1
                    continue

                # Bara rader med Failed login räknas som misslyckade inloggningar
                if "Failed login" not in line:
                    continue
                failed_count += 1

                ip = source_fields[0].split("=")[1]
                ip_counts[ip] = ip_counts.get(ip, 0) + 1
    except FileNotFoundError:
        print(f"Kunde inte hitta {file_path}. Kontrollera projektstrukturen och kör från projektroten.")
        raise SystemExit(1)
        
    return failed_count, malformed_count, ip_counts

def analyze_access_log(file_path, suspicious_ips):
    """Matchar händelser i access.log mot indikatorlistan."""
    matches = {}
    try:
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                fields = line.split()
                source_fields = [field for field in fields if field.startswith("src=")]
                if not source_fields:
                    continue
                ip = source_fields[0].split("=")[1]
                if ip in suspicious_ips:
                    matches[ip] = matches.get(ip, 0) + 1
    except FileNotFoundError:
        print(f"Kunde inte hitta {file_path}. Kontrollera projektstrukturen och kör från projektroten.")
        raise SystemExit(1)
    return matches

def main():
    # 1. Läs in indikatorer (IOC) med sökväg från konfigurationen
    suspicious_ips = load_indicators(INDICATORS_PATH)
    
    # 2. Analysera autentiseringsloggen med sökväg från konfigurationen
    failed_logins, malformed_lines, auth_ip_counts = analyze_auth_log(AUTH_LOG_PATH)
    
    # 3. Analysera webbloggen mot IOC-listan med sökväg från konfigurationen
    access_matches = analyze_access_log(ACCESS_LOG_PATH, suspicious_ips)
    
    # Hitta den IP-adress som förekommer flest gånger vid misslyckade inloggningar
    most_frequent_ip = "Ingen"
    most_frequent_count = 0
    if auth_ip_counts:
        most_frequent_ip = max(auth_ip_counts, key=auth_ip_counts.get)
        most_frequent_count = auth_ip_counts[most_frequent_ip]

    unique_ip_count = len(auth_ip_counts)
    total_ioc_matches = sum(access_matches.values())

    # Observationer byggs av resultaten (ingen fast text som kan bli fel)
    observation_lines = []
    if auth_ip_counts:
        observation_lines.append(
            f"IP-adressen {most_frequent_ip} förekommer flest gånger ({most_frequent_count} st) bland misslyckade inloggningar i auth.log.")
    else:
        observation_lines.append("Inga misslyckade inloggningar hittades i auth.log.")
    if access_matches:
        for ip in sorted(access_matches):
            observation_lines.append(
                f"{ip} finns i indikatorlistan och förekommer {access_matches[ip]} gånger i access.log.")
    else:
        observation_lines.append("Ingen adress i access.log matchade indikatorlistan.")
    observation_text = "\n".join(observation_lines)

    # 4. Bygg rapporten som ska skrivas till fil och terminal
    report_lines = [
        "==============================",
        "ITSX26 SECURITY REPORT",
        "==============================",
        "Source files: auth.log, access.log, suspicious_ips.txt",
        f"Failed logins: {failed_logins}",
        f"Unique source IPs (auth): {unique_ip_count}",
        f"IOC matches (access): {total_ioc_matches}",
        f"Most frequent failed-login source: {most_frequent_ip} ({most_frequent_count})",
        f"Malformed lines skipped: {malformed_lines}",
        "",
        "OBSERVATION",
        observation_text,
        "",
        "LIMITATION",
        "Resultatet baseras enbart på tillhandahållna textloggar och visar inte om trafiken var skadlig eller om indikatorlistan är aktuell.",
        "=============================="
    ]
    
    report_text = "\n".join(report_lines)
    
    # Skriv ut till terminalen
    print(report_text)
    
    # Skriv rapporten till output-sökvägen från konfigurationen
    try:
        with open(OUTPUT_REPORT_PATH, "w", encoding="utf-8") as report_file:
            report_file.write(report_text)
        print(f"\nRapport framgångsrikt sparad till {OUTPUT_REPORT_PATH}")
    except Exception as e:
        print(f"Kunde inte skriva till rapportfilen: {e}")

if __name__ == "__main__":
    main()

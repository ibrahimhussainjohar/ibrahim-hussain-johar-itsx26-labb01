# Security Automation – ITSX26 Kursvecka 5 (vecka 39)

## Syfte
Ett defensivt analysverktyg i Python som läser syntetiska loggfiler, räknar ett säkerhetsrelevant mönster (misslyckade inloggningar per käll-IP), jämför IP-adresser mot en indikatorlista (IOC) och skriver en reproducerbar rapport till `output/security_report.txt`.

Programmet **analyserar bara**. Det kontaktar inga externa tjänster, loggar inte in någonstans och blockerar eller ändrar ingenting. En träff är ett analysunderlag, inte ett bevis på en incident.

## Datasetval
**Dataset A (Basic).** Analyserade filer:

| Fil | Används till |
|---|---|
| `data/auth.log` | Räkna misslyckade inloggningar, extrahera käll-IP, hitta felaktiga rader |
| `data/access.log` | Matcha käll-IP mot indikatorlistan |
| `data/suspicious_ips.txt` | IOC-lista (medlemskontroll) |
| `data/firewall.log` | Finns i projektet men analyseras **inte** av programmet (se Kända begränsningar) |

Data har inte bytts under arbetet.

## Pythonversion
Python 3.14.4. Endast standardbiblioteket används, inga extra paket behövs.

## Köra programmet
Kör alltid från projektroten (mappen som innehåller `src/`, `data/` och `output/`):

```bash
cd week39-security-automation
python3 src/security_report.py
```

Rapporten skrivs ut i terminalen och sparas i `output/security_report.txt`. Mappen `output/` måste finnas. Med samma indata blir rapporten alltid identisk.

## Projektstruktur
```
week39-security-automation/
├── README.md
├── data/
│   ├── auth.log
│   ├── access.log
│   ├── firewall.log
│   └── suspicious_ips.txt
├── src/
│   └── security_report.py
├── output/
│   └── security_report.txt
└── docs/
    └── analysis.md
```

## Dataflöde
1. `load_indicators()` läser `suspicious_ips.txt` till en mängd (set) med unika IP-adresser.
2. `analyze_auth_log()` läser `auth.log` rad för rad. Rader utan `src=` räknas som felaktiga och hoppas över. Rader med `Failed login` räknas per käll-IP i en dictionary.
3. `analyze_access_log()` läser `access.log`, plockar ut `src=` och kontrollerar med `in` om IP-adressen finns i IOC-mängden.
4. `main()` sammanställer resultaten, bygger observationerna ur resultaten (ingen fast text) och skriver rapporten.

Alla indatafiler öppnas endast för läsning. Saknas en fil skrivs ett begripligt felmeddelande ut och programmet avslutas.

## Testning
Alla tester kördes mot projektets egna filer. Kontrollvärdena är räknade manuellt med `grep -c`.

| # | Testfall | Indata | Förväntat | Resultat |
|---|---|---|---|---|
| 1 | Känt positivt utfall | Originalfilerna | 4 misslyckade inloggningar, 3 IOC-träffar, 203.0.113.15 flest (3) | Stämmer |
| 2 | Noll träffar | `suspicious_ips.txt` ersatt med enbart `10.9.9.9` | 0 IOC-träffar och rapporten säger att ingen adress matchade | Stämmer |
| 3 | Formatfel / saknat fält | Raden `Malformed line without source` i `auth.log` | 1 hoppad rad, programmet kraschar inte | Stämmer (`Malformed lines skipped: 1`) |

**Manuellt kontrollvärde:**
- `grep -c "Failed login" data/auth.log` ger 4, vilket matchar programmets *Failed logins: 4*.
- `grep -c "src=203.0.113.15" data/access.log` ger 2 och `grep -c "src=198.51.100.44" data/access.log` ger 1, tillsammans 3, vilket matchar *IOC matches (access): 3*.

## Kända begränsningar
- Felaktiga rader redovisas bara för `auth.log`. Rader utan `src=` i `access.log` hoppas över utan att räknas.
- `Unique source IPs (auth)` räknar bara IP-adresser med misslyckade inloggningar, inte alla IP-adresser i `auth.log`.
- Indikatorlistans aktualitet kan inte kontrolleras. En IOC-träff säger inget om huruvida trafiken var skadlig.

## AI-redovisning
- **Verktyg:** Claude (Anthropic)
- **Vad AI hjälpte till med:** granskning av kod och om uppgiften har uppnåt krave,  README-mall]

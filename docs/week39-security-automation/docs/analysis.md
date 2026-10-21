# Säkerhetsanalys (Analysis) - Vecka 39

## 1. Rådata
Dataset A (Basic). Analysen baseras på följande filer från mappen `data/`:
* `auth.log`: Innehåller händelser för autentisering. Totalt 6 rader: 4 med `Failed login`, 1 med `Successful login` och 1 felaktigt formaterad rad utan käll-IP (`Malformed line without source`).
* `access.log`: Innehåller 4 HTTP-anrop med tidsstämplar, metoder, sökvägar och statuskoder.
* `suspicious_ips.txt`: En enkel indikatorlista (IOC) med 3 IP-adresser att matcha mot.

`firewall.log` ingår i datasetet men analyseras inte av programmet.

## 2. Metod
Programmet `src/security_report.py` läser filerna rad för rad och ändrar aldrig originalfilerna.
1. IOC-listan läses in till en mängd (set) med unika IP-adresser.
2. I `auth.log` identifieras käll-IP genom fältet `src=`. Rader utan `src=` räknas som felaktiga och hoppas över. Rader som innehåller `Failed login` räknas per IP i en dictionary.
3. I `access.log` plockas `src=` ut och kontrolleras med medlemskontroll (`in`) mot IOC-mängden.
4. Resultaten sammanställs i en rapport som skrivs till terminalen och till `output/security_report.txt`.

Resultaten kontrollerades mot manuellt räknade värden (se testfall i `README.md`).

## 3. Observation
* Programmet räknade totalt **4 misslyckade inloggningar** i `auth.log`, fördelade på 2 unika käll-IP.
* IP-adressen `203.0.113.15` förekommer flest gånger (3 gånger) bland de misslyckade inloggningarna. Den finns även i indikatorlistan `suspicious_ips.txt` och förekommer **2 gånger** i `access.log`.
* IP-adressen `198.51.100.44` har 1 misslyckad inloggning i `auth.log`, finns i indikatorlistan och förekommer **1 gång** i `access.log`.
* Totalt gav jämförelsen mot indikatorlistan **3 träffar** i `access.log`.
* **1 formateringsfel** upptäcktes och hoppades över (`Malformed line without source`). Det redovisas i rapporten och påverkar inte övriga rader.

## 4. Slutsats
Loggarna visar upprepade misslyckade inloggningsförsök från IP-adressen `203.0.113.15`, och adressen finns även i en fördefinierad indikatorlista. Det är en begränsad slutsats om vad som observerats. Den säger inte att adressen tillhör en angripare.

## 5. Osäkerhet
* Loggarna bekräftar inte vem som kontrollerar IP-adressen, eller om trafiken kom från en legitim användare, ett skript eller en förfalskad (spoofad) avsändare.
* Vi kan inte veta om indikatorlistan (`suspicious_ips.txt`) är uppdaterad eller innehåller gamla adresser.
* Datamängden är mycket liten (4 misslyckade inloggningar), så ett mönster kan inte fastställas statistiskt.

## 6. Alternativ förklaring
De upprepade misslyckade inloggningarna kan bero på en användare som har glömt sitt lösenord, eller på ett automatiserat system (t.ex. ett övervakningsverktyg eller en felkonfigurerad klient) som försöker ansluta med felaktiga uppgifter. En IP-adress kan också finnas i indikatorlistan av äldre skäl, vilket ger en falsk positiv träff.

## 7. Säkerhetsbetydelse
Träffarna utgör ett analysunderlag för vidare uppföljning. De motiverar en manuell granskning av systemets säkerhetsloggar, bland annat vilka användarkonton som angreps och om `firewall.log` visar samma adress. De ska **inte** betraktas som ett färdigt bevis på en pågående attack och ska inte leda till automatisk blockering.

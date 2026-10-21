# Säkerhetsanalys (Analysis) - Vecka 39

## 1. Rådata
Analysen baseras på följande filer från mappen `data/`
* `auth.log`: Innehåller händelser för autentisering, inklusive misslyckade inloggningar (`Failed login`) samt en felaktigt formaterad rad utan käll-IP.
* `access.log`: Innehåller HTTP-anrop med tidsstämplar, metoder, sökvägar och statuskoder.
* `suspicious_ips.txt`: En enkel indikatorlista (IOC) med kända IP-adresser att matcha mot.

## 2. Observation
* Programmet räknade totalt **4 misslyckade inloggningar** i `auth.log`.
* IP-adressen `203.0.113.15` förekommer flest gånger (3 gånger) bland de misslyckade inloggningarna och finns även med i indikatorlistan `suspicious_ips.txt`.
* **1 formateringsfel** upptäcktes och hoppades över ("Malformed line without source") i enlighet med kraven på defensiv felhantering.

## 3. Slutsats
Det finns verifierbara spår av upprepade misslyckade inloggningsförsök från en IP-adress (`203.0.113.15`) som dessutom matchar en fördefinierad indikatorlista.

## 4. Osäkerhet
* Loggarna bekräftar inte vem som kontrollerar IP-adressen eller om trafiken kom från en äktenskaplig användare, ett skript eller en spoofad avsändare.
* Vi kan inte veta om indikatorlistan (`suspicious_ips.txt`) är uppdaterad eller innehåller gamla adresser.

## 5. Alternativ förklaring
* De upprepade misslyckade inloggningarna kan bero på en användare som har glömt sitt lösenord eller ett automatiserat system (t.ex. ett övervakningsverktyg eller felkonfigurerad klient) som försöker ansluta med felaktiga uppgifter.

## 6. Säkerhetsbetydelse
Träffarna utgör ett viktigt **analysunderlag** för vidare uppföljning. De motiverar en manuell granskning av systemets säkerhetsloggar, men ska **inte** betraktas som ett färdigt bevis på en pågående attack eller leda till automatisk blockering.

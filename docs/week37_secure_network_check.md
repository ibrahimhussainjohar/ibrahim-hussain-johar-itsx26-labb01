# Del A - Miljöbeskrivning

- Ange om du använder Oracle Cloud, WSL eller Linux på PC.
Docker med ubuntu som operativ system. (Linux på PC)
Host är linux. Kör docker endast för att inte krocka med git.

- Beskriv operativsystem/distribution på en rimlig nivå.
Operativ system är en mjukvara som pratar direkt med hårdvaran och hur resusers ska utdelas.
```bash
$ uname -r
7.2.6-arch2-1
```
Operativsystem ubuntu 26.04 körs genom docker och samdelar kernel med host maskin.

- Redovisa relevanta nätverksinterface utan att publicera känsliga uppgifter.
```bash
$ ip -br a
lo               UNKNOWN        127.0.0.1/8 ::1/128
eth0@if6         UP             172.17.0.2/16
```
Det finns två nätverk inteface. Loopback och Ethernet.

- Förklara skillnaden mellan lokal adress, privat adress och publik adress där det är relevant.
Privat adressen som router har utdelat till den lokala nätverk. Publik adress har routern som kan kommunicera med resten av världen.
All trafik måste gå gneom routern innan det når målet.
Lokalt adress är loopback som pratar endast med sig själv.

- Beskriv vilka begränsningar din miljö innebär för uppgiften och vilka skillnader du observerar jämfört med
lärardemonstrationen i OCI. Skillnader är förväntade och påverkar inte bedömningen när du förklarar dem korrekt.
Docker är isolerad från resten av host machine linux. På grund av det kan jag inte av läsa hela nätverkstrafiken. Kunde inte heller sig all processor utan bara processor som på gick i själva docker kunde sig. Vilket var inte mycket, bara bash.

# Del B - Manuella Observation

| ip adress, hostname -I | Ser två interface och ipv4                                              |
| ip route               | default                                                                 |
| getent hosts           | Ja, namn med domain kan översättas till ip adress.                      |
| ss -tuln               | Porten 631 är öppet. Det används till att koppla till printer via nätet |
| curl 127.0.0.1:8080    | Kunde inte koppla med porten                                            |
| ps                     | Ser bash och ps                                                         |
# Del C - Bygg Bash Vertyg
Scriptet hittas hos /scripts/secure_network_check.sh

# Del D - Testning
Log information hittas under /evidens/

# Del E - CIA-analys
Konfidentialitet: Vilka uppgifter i nätverksutdata kan vara känsliga, och hur sanerar du dem?
Ip-adressen kan vara känsliga. Ip-adressen ändras till mot domäin namn som exempel.com för att saneras. Tar bort eventuella mac-adresser.


- Integritet: Hur hjälper loggar, versionshistorik, tydliga statusar och kontroller till att skapa tillit till resultatet?
Loggning visar vad har hänt med systemet och datum och tid är versionshistorik i loggen. Det hjälper oss att ser när saker hände i systemet.


- Tillgänglighet: Hur visar DNS, route, tjänst och port om en funktion är tillgänglig?
DNS svarar om den är tillgänglig om inte får du ingen information. Om man använder curl kommando kan man ta reda på om tjänsten fungeras. Porten kan ses med ss kommando eller curl kommando, om det svarar.



- Avvägning: Ge ett exempel där en säkerhetsåtgärd kan försämra tillgänglighet om den konfigureras fel.
Brandvägar kan stänga av en port som 22 och ssh kommer inte har tillgång att koppla.


# Del F - Reflektion och förbättring
- Vilken kontroll gav mest värde och varför?
DNS kontroll gav mest värdet eftersom med samma kommando kunde veta om internet fungerar och DNS fungerar.

- Vilken miljöskillnad påverkade ditt arbete?
Docker kunde inte se alla nätverktrafik.
Den var rätt så isolerad från resten av min host linux.
Därför kunde jag inte se vilka portar var öppet och lyssnade.


- Vilket fel var svårast att tolka?

- Vad skulle du förbättra i en version 2?
Istället för hård korda DNSen kunde man göra att scriptet fråga om namnet.


- Hur kan verktyget användas i en verklig drift- eller säkerhetsprocess utan att bli riskabelt?
Begrännsad rättigheer att använda vertyget och saneringen av logfilen innan det utdelas till andra.




# Week 36 OCI Cloud Security Lab
## 1. Linux-Vm
Namn: ubuntu

![images](images/2026-09-09_1.png)

---
## 2. Linux-kommandon

| Kommando | Vad visar det?                                                      | CIA-koppling                                                                                                                                                                                                                           |
|----------|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| whoami   | användarens namn                                                    | Konfidentialetet, rätt person ska ha åtkomst till saker till vad arbetet krävs                                                                                                                                                         |
| hostname | Namnet till vad datorn heter men kan använd vara namnet på domainet | Hostname kan avslöja vad datorn funktion är för. Därför att kan det vara lättare att filtera vilket måltavla är mest värd att attackera. Därmed riskera integritet av systemet.                                                        |
| pwd      | Visar nuvarande katalot. Var du är i fillsystemet                   | Denna kommand kan vissa en del av fillstrukturen och avslölja namn på filer som andra borde inte veta om. Vilket innebär konfidentialetet påverkas i denna instans                                                                     |
| uname -a | Visar systemet information. Vilket kernel som används               | Visar systemet information som andra borde inte veta om. Denna information avslöjar version och därmed kan veta vilka sårbarheter kan användas för det systemet. Alltså får till information som är inte behörig till, konfidentialet. |
| uptime   | Visar hur länge datorn har varit igång                              | Visar hur länge datorn har varit tillgänglig.                                                                                                                                                                                          |

---
## 3. Hardening

| Kontroll | Risk | Vad gjorde jag? | Hur verifierade jag? | CIA |
|----------|------|-----------------|----------------------|-----|
|          |      |                 |                      |     |
---
## 4. Recovery-plan
### Vad kan gå fel?
### Hur upptäcker jag problemet?
### Vad kontrollerar jag först?
### Hur återställer jag åtkomst?
### När behöver jag hjälp?
---
## 5. Backup
### Vad har jag sparat?
### Vad finns i GitHub?
### Vad kan återskapas?
### Vad går inte att återskapa?
---
## 6. Cleanup
### VM-instans
### Diskar
### Backuper
### Publika IP-adresser
### GitHub-evidens
---
## 7. CIA-reflektion
### Konfidentialitet
### Integritet
### Tillgänglighet
---
## 8. Reflektion
### Vad fungerade bra?
### Vad var svårt?
### Vad lärde jag mig?


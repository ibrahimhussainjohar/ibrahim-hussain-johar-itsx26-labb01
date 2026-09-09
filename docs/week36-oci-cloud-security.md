# Week 36 OCI Cloud Security Lab
## 1. Linux-Vm
Namn: ubuntu

![images](images/2026-09-09_1.png)

---


## 2. Linux-kommandon

| Kommando       | Vad visar det?                                                              | CIA-koppling                                                                                                                                                                                                                                                      |
|----------------|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| whoami         | användarens namn                                                            | Konfidentialetet, rätt person ska ha åtkomst till saker till vad arbetet krävs                                                                                                                                                                                    |
| hostname       | Namnet till vad datorn heter men kan använd vara namnet på domainet         | Hostname kan avslöja vad datorn funktion är för. Därför att kan det vara lättare att filtera vilket måltavla är mest värd att attackera. Därmed riskera integritet av systemet.                                                                                   |
| pwd            | Visar nuvarande katalot. Var du är i fillsystemet                           | Denna kommand kan vissa en del av fillstrukturen och avslölja namn på filer som andra borde inte veta om. Vilket innebär konfidentialetet påverkas i denna instans                                                                                                |
| uname -a       | Visar systemet information. Vilket kernel som används                       | Visar systemet information som andra borde inte veta om. Denna information avslöjar version och därmed kan veta vilka sårbarheter kan användas för det systemet. Alltså får till information som är inte behörig till, konfidentialet.                            |
| uptime         | Visar hur länge datorn har varit igång                                      | Visar hur länge datorn har varit tillgänglig.                                                                                                                                                                                                                     |
| ls -la         | Visar alla katolog och filer                                                | Visar filstrukturen och namnet på filerna. Konfidentialetet riskeras när obehörig ser.                                                                                                                                                                            |
| date           | Visar idagens datum                                                         | Kommando kan visa vilken tidzone man är på och därmed avslöja var man är världen. Med tillräckling hög privelige kan även ändras systemet datum och tid, vilket innebär det kan finnas potentiell fell sparade av tid i logfiler och därmed påverkas intergritet. |
| id             | Visar användar gruppar                                                      | Visar information om användare och group. Det ger en bild på hur systemet är uppbyggd och potentiell visar måltavla och hur man kommer in i systemet. Konfidentialet                                                                                              |
| groups         | Visar bara grupp                                                            | Visar villka gruppar finns i systemet. Kan påverka konfidentialetet.                                                                                                                                                                                              |
| ps aux \| head | Visar alla processer i systmet och även vilken användare som kör processen. | Konfidentialetet. Det finns mycket information om systemet. Vem, vad och när körs processen.                                                                                                                                                                      |

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


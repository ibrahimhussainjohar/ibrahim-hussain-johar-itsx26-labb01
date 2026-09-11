# Week 36 OCI Cloud Security Lab
## 1. Linux-Vm
Namn: ubuntu

![images](images/2026-09-09_1.png)

---

## 2. Inlogging VM

| Inloggad | Servers namn | Operativsystem     | Uptime   |
|----------|--------------|--------------------|----------|
| ibrahim  | ubuntu       | ubuntu 26.04.1 LTS | 1h 19min |


## 3. Linux-kommandon

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
| ps aux \| head | Visar alla processer i systemet och även vilken användare som kör processen. | Konfidentialetet. Det finns mycket information om systemet. Vem, vad och när körs processen.                                                                                                                                                                      |

---
## 4. Hardening

### Kontroll 1 

```bash
$ whoami
ibrahim
```
Användare `ibrahim` används i detta system.

```bash
$ id
uid=1000(ibrahim) gid=1000(ibrahim) groups=1000(ibrahim),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users),101(lxd)
```

```bash
$ groups
ibrahim adm cdrom sudo dip plugdev users lxd
```

Användare `ibrahim` tillhör i åtta grupper.

Varför ska administrativa rättigheter användas försiktigt?

Admin rättigheter ska användas försiktighet eftersom admin har full kontroll över systemet. Med dessa rättigheter kan man göra permanenta ändringar som kan skada systemet eller gör systemet urfunktion.

### Kontroll 2

```bash
$ ls -l
-rw-rw-r-- 1 ibrahim ibrahim 0 Sep 11 16:53 text.txt
```
Alla användare kan läsa filen. Bara nuvarande och de som ingår i gruppen kan skriva filen.

```bash
$ chmod 600 text.txt
$ ls -l
-rw------- 1 ibrahim ibrahim 0 Sep 11 16:53 text.txt
```
Endast användare `ibrahim` kan läsa och skriva filen.

### Kontroll 3

```bash
$ sudo apt update
88 packages can be upgraded. Run 'apt list --upgradable' to see them
```
**Varför är uppdateringar viktiga?**

Uppdateringen kan ingå säkerhetspatcher som fixar sårbarheter, buggar och systemet hålls stabilare längre. 

**Vilken del av CIA påverkas?**

Uppdateringen kan fixa sårbarheter och därmed minska risken av obehörig intrång. (Konfidentialitet).

Systemet blir mer stabilt eftersom updateringar brukar fixa buggar som orsakar krachar i applikationer. Mindre krash och användare fortsätta använda applikationen. (Tillgänglighet).

### Kontroll 4

```bash
$ ps aux | head 
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.1  0.4  24932 16288 ?        Ss   17:03   0:01 /usr/lib/systemd/systemd --switched-root --system --deserialize=51
root           2  0.0  0.0      0     0 ?        S    17:03   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    17:03   0:00 [pool_workqueue_release]
root           4  0.0  0.0      0     0 ?        I<   17:03   0:00 [kworker/R-rcu_gp]
root           5  0.0  0.0      0     0 ?        I<   17:03   0:00 [kworker/R-sync_wq]
root           6  0.0  0.0      0     0 ?        I<   17:03   0:00 [kworker/R-kvfree_rcu_reclaim]
root           7  0.0  0.0      0     0 ?        I<   17:03   0:00 [kworker/R-slub_flushwq]
root           8  0.0  0.0      0     0 ?        I<   17:03   0:00 [kworker/R-netns]
root          10  0.0  0.0      0     0 ?        I<   17:03   0:00 [kworker/0:0H-kblockd]
```

**Vilka processer verkar vara igång?**

De flesta av processer verkar vara linux kernel relaterad och systemd.

**Hur kan en oväntad process påverka systemet?**

En oväntad process kan använda mer av systemet tillgångar så att systemet blir långsammare och svårare att få tag på grejer därmed påverkar tillgängligheten. Processen kan vara kryptominer som
använder systemet tillgångar. Det kan även vara malware som samlar in information och värsta fall har rättighet att ändra information i systemet och därmed påverka både konfidentialitet och intergritet.


### Kontroll 5

```bash
$ journalctl -n 20
Sep 11 17:45:34 ubuntu systemd[1]: fwupd-refresh.service: Deactivated successfully.
Sep 11 17:45:34 ubuntu systemd[1]: Finished fwupd-refresh.service - Refresh fwupd metadata and update motd.
Sep 11 17:50:32 ubuntu systemd[1]: Starting sysstat-collect.service - system activity accounting tool...
Sep 11 17:50:32 ubuntu systemd[1]: sysstat-collect.service: Deactivated successfully.
Sep 11 17:50:32 ubuntu systemd[1]: Finished sysstat-collect.service - system activity accounting tool.
Sep 11 18:00:32 ubuntu systemd[1]: Starting sysstat-collect.service - system activity accounting tool...
Sep 11 18:00:32 ubuntu systemd[1]: sysstat-collect.service: Deactivated successfully.
Sep 11 18:00:32 ubuntu systemd[1]: Finished sysstat-collect.service - system activity accounting tool.
Sep 11 18:10:32 ubuntu systemd[1]: Starting sysstat-collect.service - system activity accounting tool...
Sep 11 18:10:32 ubuntu systemd[1]: sysstat-collect.service: Deactivated successfully.
Sep 11 18:10:32 ubuntu systemd[1]: Finished sysstat-collect.service - system activity accounting tool.
Sep 11 18:16:31 ubuntu systemd[1]: Starting fwupd-refresh.service - Refresh fwupd metadata and update motd...
Sep 11 18:16:31 ubuntu systemd[1]: fwupd-refresh.service: Deactivated successfully.
Sep 11 18:16:31 ubuntu systemd[1]: Finished fwupd-refresh.service - Refresh fwupd metadata and update motd.
Sep 11 18:17:01 ubuntu CRON[1781]: pam_unix(cron:session): session opened for user root(uid=0) by root(uid=0)
Sep 11 18:17:01 ubuntu CRON[1783]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)
Sep 11 18:17:01 ubuntu CRON[1781]: pam_unix(cron:session): session closed for user root
Sep 11 18:20:32 ubuntu systemd[1]: Starting sysstat-collect.service - system activity accounting tool...
Sep 11 18:20:32 ubuntu systemd[1]: sysstat-collect.service: Deactivated successfully.
Sep 11 18:20:32 ubuntu systemd[1]: Finished sysstat-collect.service - system activity accounting tool.
```

**Varför behöver vi loggar?**

Loggar används som spår. Vem och när gjordes vad. Om fel hände, var i systemet hände det. Loggar ger ledtråd var det gick fel och därmed blir processen till att fixa det blir lättare och snabbare.
Loggning är också för att hålla koll på att endast behörig användare har tillgång till systemet. Om loggning visar oväntat information så finns det risk att det har hänt obehöring intrång.

**Vad skulle vi leta efter om något gått fel?**

När hände felet. Har oväntat process startad. Har viktiga filer ändrat eller nya filer skapad.

### Kontroll 6

**Hur loggade du in?**

```bash
ssh-copy-id ibrahim@ip-adress
ssh ibrahim@ip-adress
```

`ssh-copy-id` kopierar ssh public key till virtual machine.
`ssh` är själva kommando som kopplar från host till virtual machine.

**Varför används SSH?**

SSH är secure shell. Det är en encrypterad koppling. Det används för att det är säker koppling och används för hantering av remote server.


**Vad skulle du göra om SSH slutade fungera?**

```bash
ping vm-ip-adress
```

Om man andra tillgång till virtual machine finns kolla `ssh` status och testa att restarta.
Kolla om port 22 är öppet i virtual machine. 
Dubble kolla om man har stavat korrekt i `ssh` kommando.
Kolla om din `ssh` nyckel finns kvar i ~/.ssh.
Testa ´ssh -v vm-ip-adress` och få mer information var någonstans kan felet finns.


---
## 5. Recovery-plan
### Vad kan gå fel?
Det går inte logga in på server.
### Hur upptäcker jag problemet?
Error message
### Vad kontrollerar jag först?
Kolla om server är på först.
Är ssh koppling time out och får error meddelande.
Kolla om ssh port 22 är öppet.
Om man direkt tillgång till server kolla ssh status och om ssh server är på.
Har jag rätt autentisering alltså ssh private nyckel och server har ekvalent offentlig nyckel

### Hur återställer jag åtkomst?
Om inget funkar går tillbaka till fungerande snapshot.

### När behöver jag hjälp?
Om man inte har direkt tillgång till server be om hjälp från leverantören.


---
## 6. Backup
### Vad har jag sparat?
En snapshot som innehåller ren installation.
En snapshot till som innehåller configurerad system.
### Vad finns i GitHub?
Har inte sparat i Github.
### Vad kan återskapas?
Kan går tillbaka till fungerande snapshot.
### Vad går inte att återskapa?
Om mycket har hänt mellan senaste snapshot och nuvarande. Därför är det viktig att skapa snapshot ofta.

---

## 7. Cleanup
Cleanup i lokalt vm är enkelt. Bara radera instansen.

---
## 8. CIA-reflektion
### Konfidentialitet
Konfidentialitet är skapa tilliten att man är den personen man påstår att vara. Det kan göras med vad man vet, lösenord, vad man har, mobil. 
### Integritet
Integritet handlar om att lita på den informationen man har kommer från rätt källa och vägen mellan transporten av informationen har inte ändrad. Det ska finnas åtgärder som gör att man kan dubble kolla om det har hänt några ändringar i information t.ex via hashsum.
### Tillgänglighet
Rätt person ska ha tillgång till informationen när det behövs.

---
## 9. Reflektion
### Vad fungerade bra?
Jag tyckte att säkerhetskontrollera gick bra.
### Vad var svårt?
Hur jag skulle tänka med cia-triaden. Den kom inte naturlig.
### Vad lärde jag mig?
Jag lärde främst om permissions. 4 är läsa, 2 är skriva, 1 är execute.


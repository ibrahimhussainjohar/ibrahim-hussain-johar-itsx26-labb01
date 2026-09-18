# Normalfall 1
```bash
$ ./secure_network_check.sh
2026-09-18T22:31:04+02:00 [INFO] Början
2026-09-18T22:31:04+02:00 [INFO] Device Interface: eth0
2026-09-18T22:31:04+02:00 [INFO] IP-adress: 172.17.0.2/16
2026-09-18T22:31:04+02:00 [OK] DNS Fungerar
2026-09-18T22:31:04+02:00 [FAIL] Localhost 8080 lyssnar inte
2026-09-18T22:31:05+02:00 [INFO] tcp: 0/0 udp: 0/0
2026-09-18T22:31:05+02:00 [INFO] Succes 1/2
2026-09-18T22:31:05+02:00 [INFO] Log file: /home/ubuntu/ibrahim-hussain-johar-itsx26-labb01/scripts/network.log
2026-09-18T22:31:05+02:00 [INFO] Slutet
```

Förväntat resultat: OK
Faktiska resultat: OK
Slutstats: Testet bekräftar att getent hosts exemple.com fungerar

# Normalfall 2

```bash
$ ./secure_network_check.sh -s
2026-09-18T22:33:06+02:00 [INFO] Början
2026-09-18T22:33:06+02:00 [INFO] Device Interface: eth0
2026-09-18T22:33:06+02:00 [INFO] IP-adress: 172.17.0.2/16
2026-09-18T22:33:06+02:00 [OK] DNS Fungerar
2026-09-18T22:33:06+02:00 [OK] Localhost 8080 lyssnar
2026-09-18T22:33:06+02:00 [INFO] tcp: 1/1 udp: 0/1
2026-09-18T22:33:06+02:00 [INFO] Succes 2/2
2026-09-18T22:33:06+02:00 [INFO] Log file: /home/ubuntu/ibrahim-hussain-johar-itsx26-labb01/scripts/network.log
2026-09-18T22:33:06+02:00 [INFO] Slutet
```

Förväntat resultat: OK
Faktiska resultat: OK
Slutstats: Med -s flagg säger till scriptet att sätta igång lokalt server och både sätta igång och lyssna fungerade.

# Felfall 1
Både DNS och Lokalt testtjänst svarar inte
```bash
./secure_network_check.sh
2026-09-18T22:35:02+02:00 [INFO] Början
2026-09-18T22:35:02+02:00 [INFO] Device Interface: eth0
2026-09-18T22:35:02+02:00 [INFO] IP-adress: 172.17.0.2/16
2026-09-18T22:35:02+02:00 [FAIL] DNS Fungerar inte
2026-09-18T22:35:02+02:00 [FAIL] Localhost 8080 lyssnar inte
2026-09-18T22:35:02+02:00 [INFO] tcp: 0/0 udp: 0/0
2026-09-18T22:35:02+02:00 [INFO] Succes 0/2
2026-09-18T22:35:02+02:00 [INFO] Log file: /home/ubuntu/ibrahim-hussain-johar-itsx26-labb01/scripts/network.log
2026-09-18T22:35:02+02:00 [INFO] Slutet
```

Förväntat resultat: FAIL
Faktiska resultat: FAIL
Slutstats: Bytte example.com till tomt och DNS fungerade inte som förväntat.


# Felfall 2
Lokal port svarat inte
```bash
./secure_network_check.sh
2026-09-18T22:36:04+02:00 [INFO] Början
2026-09-18T22:36:04+02:00 [INFO] Device Interface: eth0
2026-09-18T22:36:04+02:00 [INFO] IP-adress: 172.17.0.2/16
2026-09-18T22:36:04+02:00 [OK] DNS Fungerar
2026-09-18T22:36:04+02:00 [FAIL] Localhost 8080 lyssnar inte
2026-09-18T22:36:05+02:00 [INFO] tcp: 0/0 udp: 0/0
2026-09-18T22:36:05+02:00 [INFO] Succes 1/2
2026-09-18T22:36:05+02:00 [INFO] Log file: /home/ubuntu/ibrahim-hussain-johar-itsx26-labb01/scripts/network.log
2026-09-18T22:31:05+02:00 [INFO] Slutet
```

Förväntat resultat: FAIL
Faktiska resultat: FAIL
Slutstats: Utan flagga -s kommer inte sätta igång server och därmed porten 8080 är stängd.


# Executive summary

En kommun har fått flera mejl som verka komma från internt IT-support. Bland medarbetare har  minst en klick på en länk har hänt. Medarbetaren har uppgett att  inget information har lämnats in men detta är inte verifierad. Länken kan möjligtvis ladda ner skadliga filer som skulle kunna komprimera datorn. Länken skulle också kunna vara phishing och största risken är konfidentialitet med att angripare får åtkomst till kommunens mejl system och därmed tillgång till känsliga information. Därför bör loggar kontrolleras och MFA används till att säkerställa att angripare får inte tillgång(CIS 8 och 6). 

# Fakta, antaganden och scope

| Kategori           | Innehållet                                                                                                                                                                                   |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Givet              | Flera mejl har skickats till kommun förvaltningen som verka vara från intern IT-support. En medarbetare trykte på länken och påstår att ingen uppgift lämnades ut. Ingen bekräftad incident. |
| Antagande          | Mejlet är för phising alltså få tag på inloggningsuppgifter.                                                                                                                                 |
| Hypotes            | Länken behöver inte vara leda till falsk inloggining sida utan kan ladda ner skadliga filer. AI kan ha använt men inget grundläggande bevis på det.                                          |
| Behöver verifieras | Vad länken leder till. Om medarbetare har faktiskt inte lämnat uppgifter. Hur många i kommunen har fått mejlet. Om avsändare är extern.                                                      |
# Tillgångar och händelsekedja

- Medarbetare användarkonto
- Medarbetare klientdator
- Interna mejlsystemet
- Kommuns ärende eller persondata

Likadant mejl har skickats till flera personal i kommunal förvaltning. Mejlet liknar intern IT-support. En medarbetare tryckte på länken och leder till okänt sida (inloggning eller annat, oklart).  Om uppgifter angavs kan angripare användas till obehörig aktiviteter såsom nå känsliga information och sprida mer mejl internt via detta kapat mejl.

# CIA och enkel riskbedömning

Konfidentialitet: 

Om kontot blir kapat kan angripare har åtkomst till känsliga uppgifter och får tillgång till andra tjänster som har koppling till medarbetarens mejl identitet.

Integritet:

Angripare kan ändra regler eller inställningar i kontot utan tillstånd. Skicka mejl till andra med falska information.

Tillgänglighet:

Kontot kan spärrat ut medarbetaren. Om länken laddar ner skadlig fil så kan datorn behöver isoleras.

|             | Bedömning      | Motivering                                                                       |
| ----------- | -------------- | -------------------------------------------------------------------------------- |
| Sannolikhet | medel          | Flera mejl skickade och en bekräftad klick. Finns chans att fler klickade också. |
| Konsekvens  | medel till hög | Beroende på behörigheten av användare.                                           |
| Total risk  | medel          | Nuvarande inte stor risk men om loggarna visar avvikande bör den höjas.          |
# CIS-mappning

CIS 6: Om angripare får inloggningsuppgifter så kan MFA stoppa åtkomsten till mejlkontot. Kontot ska ha minsta behörighet den kan ha för att minska angriparnas attack yta.

CIS 8: Loggar som inloggning, mejl och proxy kan kontrollera medarbetarens påstående.

CIS 14: Träning inom säkerhet och verifiera om IT-support verkligen har skickat mejlet.

# Prioriterade åtgärder

Granska loggar, kontroller inloggningar efter klicktillfället, byt lösenord och logga ut från all sessioner. 

Använd MFA

Träning och ber om att verifiera när mejlet verkar vara från  internt IT-support. Verifiera med falska phishing så att veta om träningen har varit effektiv.

# Teknisk koppling

När länken trycktes då måste datorn slå upp domännamnet vis DNS. Om man har tillgång till DNS-loggar kan man se vilken domän som slog upp och när. Sedan kan domänen kontrolleras om det finns, vilken IP-adress pekar den på och liknar den kommunens egen domän. 

Porten kan också kollas om den är blev ansluten till 443 eller annat port. Om kommunen använder vanligtvis 443 så kan detta vara en markör för avvikelse. Porten säger inget om sidan är skadlig.

# English Security Summary

A municipal department got several email. Sender seems to be internal IT support. At least one employee clicked the link that was contained in the mail. The employee assures that no information was given but this is unverified. The link could lead to false site meaning a phishing attempt, could also be that the link download a dangerous file with the potential to compromise the computer. The biggest concern of phishing is confidentiality where the attacker will have access to sensitive information. That is why the logs should be controlled and MFA is used to ensure that the attacker does not have access (CIS 8 and 6)
# AI- och källredovisning

**Verktyg:** Claude (Anthropic).

**Användning:** Jag använde Claude för att förstå uppgiftens krav, få en struktur för rapporten och få feedback på mina utkast. Rapportens text är skriven av mig, med vissa formuleringar och exempel från Claude som jag skrivit om.

**Verifiering:** Jag kontrollerade CIS-kontrollernas namn mot CIS officiella dokument (v8.1).

**Fel och korrigeringar:** Claude föreslog en teknisk koppling som byggde på moment som vi inte hade gjort i kursen. Jag rättade det och skrev utifrån vad vi faktiskt gjorde: ett skript för DNS och port samt Wireshark. Jag la också till en egen hypotes om att länken kan ladda ner skadlig fil och att åtgärden ska verifieras med en phishingsimulering. Claudes förslag på riskbedömning har jag motiverat själv utifrån caset.

Källhänvisning:

CIS-kontroller - kursmaterial

CIS v8.1: https://www.cisecurity.org/controls/v8-1

# Slutsats
Risken bedömer jag som medel. Flera mejl har skickats och minst en medarbetare har klickat på länken, men det finns ingen bekräftad inloggning eller intrång. Den viktigaste åtgärden är att granska loggar för det berörda kontot, för att se om medarbetarens uppgift stämmer. Därefter minskar MFA och rollanpassad träning risken för framtida liknande händelser. Kvarvarande osäkerhet är vart länken leder, om fler har klickat och om AI har använts, vilket inget i underlaget visar. Bedömningen bör ses över om loggarna visar avvikande inloggningar eller om en skadlig fil hittas.

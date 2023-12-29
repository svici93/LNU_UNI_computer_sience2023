************************


# Mini-projekt Rapport
Medlemmar: Simon Vilmi och Theo Schön  
Program: Datateknik och Elektroteknik  
Kurs: 1DV501  
Inlämningsdatum: 2023-11-02  


## Introduktion
Följande projekt innebar ett sorts slutprojekt för kursen "Introduktion till Programmering" eller 1DV501. Projektet var strukturerat som ett mindre grupparbete med 1-2 personer där själva uppgiften var indelad i flera steg. Målet med just vårt projekt var att undersöka och arbeta med både Hashing och ett Binary Search Tree (BST). I detta projektet använde vi oss av tidigare material, nämligen output texterna från två uppgifter i Assignment 3. Dessa texter har döpts till "brian" och "swe_news".


Syftet med detta projektet var att ge grund och vidare vidga våra kunskaper i programmering för att vi i senare kurser ska bli bättre förberedda för tuffare och större uppgifter.


De specificerade uppgifts instruktionerna var följande:


Steg 1: Använd pythons set och dictionary class för att beräkna antal unika ord i de båda texterna och även producera en topp 10 lista med de mest frekventa orden.


Steg 2: Implementera två dataklasser passande till att arbeta med ord som data. Ett hash baserat set och ett Binary Search Tree (BST).


Steg 3: Repetera steg 1 fast med de nya data klasserna implementerade i steg 2.


## Part 1: Count unique words 1
Uppgiften här var att använda sig av pythons set och dictionary för att räkna antal unika ord i filerna “brian” och “swe_news”.


### Antal ord per fil:
“brian”: 13380  
“swe_news”: 15099647  


### Topp 10 frekventa ord
Första steget var att introducera en funktion som beräknar frekvensen för varje ord. Detta gjordes genom att först öppna en tom “Dictionary” som lagrar frekvensen för varje ord i den fil som angetts.
```python
for line in file:
    words = line.strip().split()
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
```
Med hjälp av första “for” satsen delas varje ord upp för sig och läggs till i en lista “words”. Sedan med hjälp av den andra “for” satsen räknas varje ord i listan igenom och för varje dubblett den stöter på uppdateras värdet för det ordet med +1. Och på så sätt kan den räkna hur många gånger ett ord finns i textfilen. Sedan sorteras varje ord i dictionary:t efter de mest frekventa och funktionen returnerar de tio mest frekventa orden.


### Resultaten


Antalet unika ord i båda filerna: 463027


Topp 10 frekventa ord för “brian”  
the: 374  
brian: 366  
you: 299  
a: 248  
i: 219  
to: 192  
and: 181  
in: 179  
man: 174  
of: 171  


Topp 10 frekventa ord för “swe_news”  
i: 484015  
att: 436447  
och: 430813  
det: 299963  
på: 281224  
som: 277833  
en: 267134  
är: 245607  
för: 223381  
av: 191829  


## Part 2: Implementing data structures
Uppgiften gick ut på att definiera en datastruktur eller hashset,  som skulle användas för att lagra en samling ord samt utföra en rad olika operationer med hjälp av datan.
Ett hashset eller en hashuppsättning kan beskrivas som en lista av buckets/hinkar där varje hink innehåller en lista av ord. Storleken skulle initialt bestå av 8 st hinkar men skulle ändras dynamiskt allt eftersom behovet av mer plats ökade. D.v.s när data lades till i uppsättningen.
För att detta ska fungera behövdes en rad funktioner som “add”, “rehash”, “remove” m.fl. Som beskrivs mer i detalj nedan.

### Add, Get_hash och Rehashing
Funktionen “add” i hashset-klassen lägger till data i form av strängar i hashuppsättningen.
Funktionen tar emot en sträng som parameter och skickar vidare den strängen in i funktionen get_hash som beräknar ett hashvärde för strängen enligt en given formel. Värdet kan sedan användas för att bestämma i vilken bucket som strängen skall sparas i. En indexering för placeringen skapas med hjälp av att använda hashvärdet % len(self.buckets). Funktionen lägger endast till strängar som inte redan finns i hashuppsättningen, d.v.s unika strängar.


Funktionen get_hash används för att beräkna ett hashvärde för en given sträng. Funktionen åstadkommer detta genom att loopa igenom samtliga tecken i strängen och för varje tecken multipliceras det nuvarande hash-värdet med 31 för att sedan addera tecknets Unicodevärde.
Detta genererar en unik hashkod för varje ord baserat på dess tecken.


Rehashing utförs när storleken på hashupsättningen blivit lika med eller större än antalet buckets. Rehashing sker genom en funktion rehash(), och innebär följande, Alla strängar som för tillfället finns i hashuppsättningens befintliga buckets samlas och sparas i en temporär lista “lst” och sedan fördubblas antalet buckets genom att initiera en ny tom lista med dubbelt så många buckets som förut. därefter läggs strängarna i “lst” återigen tillbaka i nya buckets.
vilket innebär att slutligen har vi fått en ny uppsättning buckets som är dubbelt så stor och samtliga data är fortfarande kvar. Rehashing är nödvändigt för att bibehålla en rimlig belastning i hashuppsättningen.



Vi fick väldigt liknande resultat som de givna resultaten i programmet hash_main.py, det som skiljde sig åt i våra resultat var max_bucket som var ger 5 för våran kod, och gav 3 för den givna koden. Detta kan bero på hur datan läggs till i hashuppsättningen och kan t.ex. bero på att våra algoritmer för att beräkna hashvärde kan ha sett något olika ut.

### Put och Max_depth
Funktionen put används för att lägga till ett key-value-par i sökträdet, funktionen är en rekursiv funktion som används för att lägga till nya värden i BST. I detta fallet används den rekursiva funktionen för att använda funktionen fast från en ny “position” i trädet. BST eller ett “Binärt sökträd" fungerar på så sätt att du bygger ett träd med dina värden som utgår en så kallad root-nod som kan ha upp till två noder under sig, varje nod i trädet kan ha upp till två grenar eller noder under sig. Funktionen Put börjar med att kontrollera ifall det finns en root-nod och om det inte finns så läggs det givna värdet till där, om det finns en root-nod så jämför funktionen värdet som finns i root-noden och värdet som ska läggas till. Det första funktionen gör är att kolla ifall det givna värdet är större, lika med eller mindre än det befintliga värdet, om det är större kommer funktionen att kolla noden till höger om den nuvarande noden och se ifall den har ett värde och om det inte finns ett värde så kommer det givna värdet att tilldelas till den noden, om det däremot finns ett värde kommer funktionen att återkallas därifrån. Samma sak sker då det givna värdet är mindre än det befintliga värdet fast åt vänster istället. Om det givna värdet varken är större eller mindre än det befintliga så kommer noden att uppdateras med det givna värdet. Och så fortsätter funktionen att återkalla sig själv tills den hittar en tom plats i trädet för det givna värdet.


max_depth funktionen används för att beräkna det maximala djupet av trädet. D.v.s  antalet noder från root-noden till den nod som är längst bort. Om trädet är tomt är max_depth = 0.
Om trädet inte är tomt så delegeras beräkningen av djupet genom att rekursivt jämföra djupet av vänster och höger nodträd för att sedan returnera det största värdet(djupet) + den aktuella noden.

Vi fick exakt samma resultat som de givna resultaten i bst_main.py
## Part 3: Count unique words 2

* Programmet implementerar funktionen genom att använda klassen BstMap (en binär sökträdskarta). Programmet börjar skapa ett klassobjekt/instans av klassen BstMap som kallas för word_frequency för att lagra varje unikt ord i samma instans av denna “kartan” . Sedan läses filerna in var för sig och orden delas upp med . strip().split() och alla ord sparas i en lista “words”, Sedan itereras över denna lista och alla ord läggs till i kartan med funktionen put(), där ordet som nyckel samt dess frekvens som värde. Om ett ord inte finns läggs dess initiala frekvens till 1, om ordet finns ökas frekvensen med 1 o.s.v.  sedan för att sortera och skriva ut de 10 mest frekventa orden anväds BstMap-klassens funktion as_list för att hämta samtliga nyckelpar som lista och sorteras sedan med .sort() metoden. för att sortera efter frekvensen. För att sedan skriva ut de 10 mest frekvent förekommande orden används en for-loop för att loopa igenom de 10 första elementen i den sorterade listan och skriva ut varje ord, frekvens.


### Topp 10 Resultat
Topp 10 frekventa ord för “brian”  
the: 374  
brian: 366  
you: 299  
a: 248  
i: 219  
to: 192  
and: 181  
in: 179  
man: 174  
of: 171  


Topp 10 frekventa ord för “swe_news”  
i: 484015  
att: 436447  
och: 430813  
det: 299963  
på: 281224  
som: 277833  
en: 267134  
är: 245607  
för: 223381  
av: 191829  

### Resterande Resultat
* Bucket list size: 524288  
* Max bucket size: 8  
* Zero bucket ratio: 0.5  
* Number of tree nodes: 462039  
* The maximum depth of the tree: 129  
* Internal node count of the tree: 462038  


### Max Bucket Size och Zero Ratio Bucket
Max bucket size representerar den största mängden element som finns i någon av hashuppsättningens buckets. Detta värde kan användas för att bedöma hur jämnt hashfunktionen fördelar elementen över de olika buckets som uppsättningen har. Optimalt är om max bucket size ganska litet då detta är en indikation på en jämn fördelning av elementen över hinkarna/buckets. Men ett optimalt värde beror också på applikationen och datan. Ett rimligt värde är något högre än det förväntade värdet men inte allt för stort. Ett dåligt värde är ett högt värde som innebär att många buckets är tomma och tyder på en inneffektiv hashfunktion som inte fördelar elementen jämnt.
### Max Depth och Internal Node Count
Max depth representerar längden på den längsta vägen från roten till löv i sökträdet, och kan användas för att bedöma hur balanserat sökträdet är. Ett träd som har en balanserad struktur har ett ganska lågt maxdjup då alla löv ligger på samma djupnivå. Ett rimligt resultat beror såklart på mängden data som finns i trädet men värdet bör vara relativt lågt. Ett dåligt strukturerat träd har ett större värde på max depth och gör att sökningar blir ineffektiva och tar lång tid.


internal node count räknar antalet noder i sökträdet som har minst 1 barn. Detta ger en indikation på trädets struktur och komplexitet. Som gällande de övriga värderna så eftersträvas här också ett så lågt värde som möjligt då det innebär en bälbalanserad struktur med lite överflödig komplexitet. Ett rimligt värde kan vara något högre men inte allför högt då det indikerar på en ineffektiv struktur.


## Project conclusions and lessons learned
We separate technical issues from project related issues.
### Technical issues

Som tur var så stötte vi inte på allt för mycket tekniska problem, mestadels så var det problem med gitlab om man till exempel hade glömt att dra en git pull innan man började arbeta, men det var ingenting vi inte kunde lösa relativt snabbt. Det är klart att vi stötte på mindre stop under tiden vi programmerade, till exempel blev vi rätt snopna då vi inte fick funktionen “count” att fungera som vi hade tänkt då vi tänkte att den kallades genom bst.Node och inte bst.BstMap som de tidigare funktionerna. Detta var inget långvarigt problem då vi höll en bra kommunikation och konsulterade över problemet vilket ledde till en rätt snabb lösning.

Det vi har lärt oss är att det bästa hade varit att börja på projektet lite tidigare så vi hade kunnat ägna oss åt kortare mer uppdelade intervall av att arbeta då detta arbetet krockade lite med en mattetenta, men hade vi haft mer tid tror jag inte att vårt resultat hade förbättrats allt för mycket då detta blev rätt bra, däremot tror jag att vi hade haft mer tid att strukturera koden 

### Project issues

Vi kommunicerade flitigt via SMS och deligerade inte arbetet allt för mycket på förhand. Vi skrev mest till varande att "Jag gör dessa delar nu" och så pratade vi ifall vi fastnade någonstans eller hade några andra frågor.

- Theo  
Simon var den som började arbeta först av oss två och var därmed den som bidrog till en majoritet av arbetet i de första stegen av projektet, sedan hjälptes vi åt att konstruera resten av uppgifterna både genom att sitta själva och genom att kommunicera över SMS vad som ska göras och hur det görs på bästa sätt.

- Simon  
Arbetet har varit både roligt och lärorikt, att sammarbeta via gitlab  i ett gemensamt projekt har givit mig nya kunskaper, Jag har också fördjupat mina kunskaper om och förståelse för datastrukturer och hur de kan användas.
Sammarbetet mellan Theo och mig har fungerat väl, och vi har båda genom hela arbetet aktivt och frekvent samarbetat med projektet, vi har gemensamt diskuterat problem och lösningar som drivit projektet framåt.  

Den totala tiden spenderat på det här projektet skulle ungefär kunna mätas upp till ca 10 timmars arbete var där en majoritet gjordes nu under inlämningsveckan. Så den totala arbetstiden nedlagd kan konstateras vara ungefär 20 timmar.

Angående sätt att arbeta fanns det inte jättemycket att ta med sig, olika personer föredrar olika sorter av arbetsstruktur och denna sorten där vi mestadels jobbar enskilt och konsulterar varandra fungerade väldigt bra för oss under detta arbetet.



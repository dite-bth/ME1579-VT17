# Övningar grundläggande SQL

Syftet med de här övningarna är att ska bekanta dig med grundläggande SQL-kommandon.
Använd World-databasen, som är en exempel-databas som MySql tillhandahåller.
Du kan ladda ner databasen som en fil direkt ifrån deras site; logga in på din RPi och kör följande kommando i terminalen;
$ wget http://downloads.mysql.com/docs/world.sql.zip


Du packar upp .zip-filen med kommandot;
$ unzip world.sql.zip

För att konstruera alla tabeller med all data i MySql så kör vi följande inne i MySql;
mysql> SOURCE /home/pi/world.sql
(ovan förutsätter att du packat upp filen i din hemmakatalog)

Om du skulle ‘förstöra’ databasen så är det bara att köra ovan kommando igen. Möjligtvis att du behöver ta bort databasen först, vilket kan göras med DROP DATABASE world.


Konstruera SQL-kommandon, som kan visa svarsdata/svarstabeller, för var och en av nedanstående punkter. Spara gärna dina kommandon i en (eller flera) filer så att du kan gå tillbaka till dem senare. I de fall frågorna gäller t ex att skapa ett ER-diagram så spara gärna även det som t ex pdf eller en bild.

Du behöver inte göra alla övningarna - om du känner att du behärskar, gå vidare till nästa.



1. Skriv kommandot för att skapa databasen world.


2. Visa alla tabeller i databasen.


3. Visa alla städer i ett valfritt land.


4. Vilka städer i har mer än 10 000 000 invånare?


5. I vilket distrikt ligger den stad som har mest invånare? Visa endast just det distriktet.

6. Hur många städer finns det i USA?

7. Hur många städer i Japan har fler än 1 miljon invånare?

8. Hur många invånare, totalt, finns det i Indien?

9. Visa namn, distrikt och population för alla städer i Sverige.

10. Det verkar som om distriktet i vilket Stockholm ligger är fel... Rätta till felet så att Stockholm får rätt distrikt (län). Gör det med korrekt sql-kommando.

11. Lägg till 10st valfria orter i Sverige.

12. Ta bort alla städer i Sverige.

13. Vem är president i USA? Stämmer verkligen det? Rätta till felet.

14. Hur många länder har Spanska som icke officiellt språk?

15. Visa alla städer vars population är mer än genomsnittliga populationen (för alla städer i databasen).

16. Vad blir den sammanlagda summan av procentsatsen, av de länder vars officella språk är engelska? 
    Visa summan på samma sätt som i figuren nedan. x och y är siffror som visar exakt summa;<br>
+----------------------------+<br>
| Summa kardemumma           |<br>
+----------------------------+<br>
|   xxx.y                        |<br>
+----------------------------+<br>

17. Visa med lämplig JOIN för alla städer; städernas namn, landet städerna ligger i samt vilket språk som talas. Ordna resultatet först efter landets namn och sedan stadens namn. Ditt statement ska innefatta alla tabellerna.

18. Skapa en tabell som kan innehålla data för alla län i Sverige. Skriv in korrekt sql för tabellen. Glöm inte primärnyckel (PK) och andra eventuella nycklar som kan behövas. Åtminstone en FK ska finnas med.

19. Gör en ER-modell och en fysisk modell av world-databasen. Lämna in i pdf eller som en bild.

20.Gör ett statement som skapar en temporär tabell i minnet som innehåller de tio städer som har flest invånare från tabellen City. Tabellen ska heta Population10 och innehålla samma kolumner med data i, som tabellen City, för dessa 10 städer. 

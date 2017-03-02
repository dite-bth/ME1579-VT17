# Mer övningar, grundläggande SQL

För dessa övningar krävs databasen classicmodels.
Importera in den i din MySql på din Raspberry Pi;

`mysql>SOURCE /home/pi/dinFil.sql`

Databasen finns i detta repot i form av filen **classic.sql**.





**SELECT**

1. Utgå från tabellen *employees* och konstruera SQL-kommandon som ett svar på följande;

- Visa alla anställda med anställningsnummer, förnamn, efternamn, email och vilken titel respektive anställd har.


-  Hur många anställda finns totalt?

-  Hur många anställda heter Firrelli?

 - Visa alla anställdas efternamn - ta bort eventuella dubbletter (om flera har samma efternamn så ska det endast visas en gång).

 - Visa alla anställda (förnamn och efternamn) vars jobbtitel är Sales rep.

 - Visa alla anställda (förnamn, efternamn och jobbtitel) som är högsta chef (President) eller chef för Sales (VP Sales).

 - Vilka anställda har Gerard Bondur som chef? 
   Visa detta på åtminstone 2 olika sätt (gör 2st olika SELECT queries).

 - Visa alla anställda (förnamn, efternamn och officeCode) vars officeCode är större än 2.

     ​

     Utgå från tabellen *offices* för nedanstående;

2. Visa information för dom kontor som finns i USA och Japan. Använd **IN**.

3. Visa information om kontoren i bokstavsordning utifrån staden dom är lokaliserade i.

4. Som ovan, fast omvänd ordning.

   ​

   Utgå nu från tabellen *customers*;

5. Visa information om de kunder vars namn startar med strängen "Dan".

6. Hur stor är den genomsnittliga kreditbegränsingen (creditLimit) för de kunder som finns i USA? Svaret ska visas med 2 decimaler. 

   ​

   Utgå nu från tabellerna *customers* och *employees*;

7. Vilken anställd ansvarar för/har hand om vilken kund (customer.salesRepEmployeeNumber)?
   Visa kundens namn, den anställdas id samt den anställdas för-, och efternamn.
   Tips: INNER JOIN.

   ​

   Utgå från tabellerna *customers* och *orders*;

8. Visa alla ordrar, med dess statusar, som tillhör respektive kund. Visa kundnummer, kundens namn, ordernummer och orderstatus. 
   TIPS: Använd LEFT JOIN.
   ​

9. Visa alla kunder som inte har lagt någon order. Visa kundnummer, kundnamn, ordernummer och orderstatus (både ordernummer och orderstatus ska alltså vara NULL).
   Använd LEFT JOIN på customers och orders.

   ​

10. Använd dig av tabellerna employees och offices. Konstruera ett SELECT-kommando som innehåller en subquery och ger följande resultat;
   visar de anställda vars kontor ligger i Japan.
   ​

11. _Extra/frivillig:_
   Visa med en subquery och aggregate functions vilka kunder vars amount i tabellen payments överstiger medelsnittet för just amount i payments.
   ​

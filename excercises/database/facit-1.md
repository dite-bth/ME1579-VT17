1. CREATE DATABASE world;
2. SHOW tables;
3. SELECT * FROM City WHERE CountryCode = ‘USA’;
4. SELECT * FROM City WHERE Population > 10000000;
5. SELECT District  FROM City ORDER BY Population DESC LIMIT 1;
6. SELECT COUNT(*) From City WHERE CountryCode='USA';
7. SELECT COUNT(*) From city WHERE CountryCode='JPN' AND Population > 1000000;
   11 st
8. SELECT SUM(Population) From city WHERE CountryCode='IND';
   123298526st
9. select name, district, population from city where CountryCode = "SWE";
10. UPDATE CITY SET DISTRICT=”Stockholms län” WHERE ID=3048;
11. INSERT INTO CITY VALUES(4080, ‘Namn’, ‘SWE’, ‘distrikt’, 50500);
12. Glöm inte ta backup först.
    DELETE FROM City WHERE CountryCode=”SWE”;
13. SELECT HeadOfState FROM country WHERE code='USA';   -- George W. Bush
    UPDATE country SET HeadOfState='Donald Trump' WHERE code='USA';
14. SELECT COUNT(*) from CountryLanguage WHERE IsOfficial ="F" AND Language="Spanish";
15. SELECT Name FROM City Where Population > (SELECT AVG(Population) FROM City);
    875 stycken
16. SELECT SUM(Percentage) AS ‘Summa kardemumma’ from CountryLanguage WHERE IsOfficial ="T" AND Language="English"; Summan är 955.7
17. SELECT City.Name, Country.Name, CountryLanguage.Language FROM City INNER JOIN Country ON City.CountryCode=Country.Code INNER JOIN CountryLanguage ON CountryLanguage.CountryCode=Country.Code ORDER BY Country.Name, City.Name;
18. ...
19. ...
20. CREATE TABLE Population10 engine=MEMORY SELECT * FROM City ORDER BY Population DESC LIMIT 10;






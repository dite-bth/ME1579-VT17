# Övningar relations-databas (MySql)



Här finns övningar att göra för hantering av relationsdatabasen MySql.
Använd helst terminallägget (dvs arbeta med mysql i en terminal/konsoll) för att lära dig exakt syntax och kommandon för att navigera i en databas.

Börja med antingen 1-excercises-db.md eller 2-excercises-db.md eller arbeta med bägge parallellt (dom innehåller ungefär samma typ av övningar). 

1-excercises-db.md, använder world-databasen, som du enligt instruktioner importerar in i din databas.

2-excercises-db.md - använder en annan databas som finns i detta repo (classic.sql).




Filen `db-script.sh`, i den här mappen, är ett bash-script som laddar ner och installerar de databaserna som används i övningarna.
Du kan alltså använda den på en linux-maskin (t ex din RPi eller i en Vagrant) för att installera databaserna. Notera att du behöver ha MySql installerat. Ställ dessutom in rätt värden i .sh-filen så att det matchar dina användare i MySql.
För att göra den körbar (efter nedladdning);

`$ chmod a+x db-script.sh`

kör scriptet med;

`$ ./db-script.sh` 

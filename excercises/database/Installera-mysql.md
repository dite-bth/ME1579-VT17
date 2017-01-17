# Installera MySql-server



Instruktionerna är riktade till Linux (Raspberry Pi).



**Installation**

Noteras bör att MySql tar en del hårddisk (ca 90MB) samt processorkraft. 
Ett likvärdigt alternativ till MySql är den helt open-source MariaDb. 

Logga in i en terminal på din RPi och installera MySql med följande kommando;

`$ sudo apt-get install mysql-server`

Ovan kommando installerar databas-servern (dock inte klient-delen).
Under installationen får du ange ett lösenord för root-användaren (adminstratörs-kontot) till MySql.



**Skapa en användare som inte är root **

Det är rekommenderat att skapa en användare som inte är root (av säkerhetsskäl). Denna användare kan sedan ges behörighet till specifika databaser i MySql och kan användas när du programmerar.

Logga in i MySql, via terminalen, på den host den är installerad på. Ange lösenordet du angav vid installationen;

`$ mysql -uroot -p`

För att skapa en ny användare i MySql;
`mysql> CREATE USER 'USERNAME'@'localhost' IDENTIFIED BY 'MY_PASSWORD';`
där USERNAME och PASSWORD byts ut mot egna värden för användarnamn respektive lösenord.

För att ställa in vilka databaser en användare ska ha behörighet till så görs det med ett kommando i mysql;
`mysql> GRANT ALL PRIVILEGES ON MY_DATABASE.* TO 'USERNAME'@'%' IDENTIFIED BY 'PASSWORD';`

där användarnamnet och lösenordet anges. MY_DATABASE är den databas man vill ge behörighet till; om man istället anger * som namn på databas , så ges behörighet till allt. % efter användarnamn@ anger från vilket ip (host) användaren får ansluta - i detta fallet betyder det att anslutning kan göras från var som helst.
Exempel;
`mysql> GRANT ALL PRIVILEGES ON *.* TO 'USERNAME'@'%' IDENTIFIED BY 'PASSWORD';`



*för att skapa en databas i MySql;*

`mysql> CREATE DATABASE MY_NEW_DATABASE_NAME;`


*för att se aktuella behörigheter;*
`mysql> SELECT * from information_schema.user_privileges where grantee like "'USERNAME'%";` 

*för att ta bort en användare i MySql:*

`mysql> DROP USER 'USERNAME'@'localhost';`

*för att ta bort behörigheter för användare;*
`mysql> REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'USERNAME'@'%';`
 


**Glömt root-lösenordet?**

Se här: https://debian-administration.org/article/442/Resetting_a_forgotten_MySQL_root_password



**Ansluta till MySql från en annan host**

*På maskinen du har mysql-server installerad;*
ändra i filen /etc/mysql/my.cnf, leta upp raden som lyder;
`bind 127.0.0.1` vilken gör att man bara kan ansluta från samma host som mysql är installerad på.
Ändra raden till;
`bind 0.0.0.0` så kan man ansluta från varifrån som helst.

Starta sedan om MySql så att den nya konfigurationen läses in;
`$ sudo service mysql restart`.

Som en säkerhetsåtgärd bör man se till att root-användaren inte kan ansluta från andra hosts. 



*På den maskin du vill ansluta till mysql;*
installera mysql-client; `$ sudo apt-get install mysql-client`
anslut nu med -h parametern;
`$ mysql -uUSERNAME -h ip-till-maskin-med-mysql-servern -p`

Du kan också använda andra verktyg för att ansluta till MySql. Exempelvis MySql Workbench. Det finns t o m extensions till Chrome.



**Avsluta MySql**

Avsluta MySql genom att skriva quit;  `mysql> quit`.



**Köra en extern .sql-fil (importera data och databas från fil etc)**

Använd kommandot SOURCE och ange den absoluta sökvägen till din .sql-fil. Exempel;
`mysql> SOURCE /home/username/mySuperData.sql`

eller på Windows;
`mysql> SOURCE C:/data/mySuperData.sql`



**Kopiera databas till/från en annan server**

Säkert (med SSH):

`$ mysqldump -h [server] -u [user] -p[password][databasename] | ssh [ssh_username]@remote_domain.com mysql -u [user] -p[password][databasename]`

Osäkert:

`$ mysqldump -h [server] -u [user] -p[password][databasename] | mysql -h [server] -u [user] -p[password][databasename]`



Om du bara vill kopiera en tabell (inte hela databasen, som ovan):

`$ mysqldump -h [server] -u [user] -p[password][databasename] [tablename] | mysql -h [server] -u [user] -p[password][databasename]`





**Länkar:**

[http://www.raspberry-projects.com/pi/software_utilities/web-servers/mysql]: http://www.raspberry-projects.com/pi/software_utilities/web-servers/mysql	"MySql RPi setup"
[https://debian-administration.org/article/442/Resetting_a_forgotten_MySQL_root_password]: https://debian-administration.org/article/442/Resetting_a_forgotten_MySQL_root_password	"Reset MySql Root password"

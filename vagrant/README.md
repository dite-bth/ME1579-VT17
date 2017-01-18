# Vagrant





[TOC]







### Installation



Installera Vagrant samt Virtualbox;

- https://www.vagrantup.com/
- https://www.virtualbox.org/



### Starta

Starta en terminal och navigera till den mapp där du vill dra igång din virtuella maskin.
Det finns olika sätta att starta/skapa en maskin, varav ett innefattar kommandot för att initiera en konfiguration för en maskin (i detta fallet ubuntu 14.04);

`$ vagrant init ubuntu/trusty64`

En `Vagrantfile` skapas i mappen. Denna fil kan sedan modifieras efter behov, exempelvis direktivet;

`config.vm.box = "ubuntu/trusty64"`

där man anger det OS man vill köra (i ovan exempel Ubuntu 14.04 LTS, Trusty, 64bitars).
Om man inte sedan tidigare gjort just en sådan maskin så laddas den ner.

Efter det kan man starta sin maskin, i en terminal i den mapp där Vagrantfile finns;

`$ vagrant up`

Efter maskinen startats loggar man in i den med;

`$ vagrant ssh`



Läs mer här; https://www.vagrantup.com/docs/getting-started/



### I det här repot

Finns en Vagrantfile för en ubuntu 14.04 LTS amd64 maskin.
Portarna 8080 och 3333 på din host, mappas mot 80 respektive 3306.

I maskinen delas mappen /vagrant till din host.



Några saker installeras från början (enligt setup.sh), bland annat MySql-server och python3.

I scriptet pip-venv.sh, som kan köras efter man skapat maskinen, så installeras pip3 samt virtualenv.

### virtualenv i /vagrant

För att arbeta med en virtueln environment med python i /vagrant-mappen (som ju delas till din host), så gör nya venvs med kommandot;

``````
$ cd /vagrant
$ mkdir myNewFlaskApp && cd myNewFlaskApp
$ virtualenv --always-copy myNewEnv               # vi måste ha med --always-copy
``````

notera att argumentet --always-copy måste vara med - annars uppstår ett fel, vilket beror på att en shared-folder skapas av virtualbox, vilken innehåller en den begränsningar.



### Vagrant share

Ett bra verktyg i vagrant är vagrant share, med vilket man kan dela ut en webb-server (från en vagrant-maskin) till _vem som helst_. Man kan dela ut vilken port som helst.
Läs mer: https://www.vagrantup.com/docs/share/

För detta behöver man ett konto på http://atlas.hashicorp.com

För att dela;

logga först in med ditt atlas-konto;

`$ vagrant login`

- **port 80** - webbserver
  boota din maskin och;
  `$ vagrant share`

- **ssh** - port 22
  boot maskinen och;
  `$ vagrant share --ssh`
  ange ett password. Du får ett s.k _share name_ som du delar ut till den som ska ansluta.
  Anslut med;
  `$ vagrant connect --ssh SHARE-NAME`

- **dela valfri port**
  t ex 3306. Boota din maskin och kör;
  `$ vagrant share --disable-http`

  _notera att de portar som specificerats i din Vagrantfile är dom som delas_


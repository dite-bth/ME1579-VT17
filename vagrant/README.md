# Vagrant



### Installation



Installera Vagrant samt Virtualbox;

- https://www.vagrantup.com/
- https://www.virtualbox.org/



### Starta

Starta en terminal och navigera till den mapp där du vill dra igång din virtuella maskin.
Det finns olika sätta att starta/skapa en maskin, varav ett innefattar kommandot;

`$ vagrant init`

där en `Vagrantfile` skapas i mappen. Denna fil kan sedan modifieras efter behov, exempelvis direktivet;

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




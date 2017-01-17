#!/bin/bash

DB_ROOT_PASS=password123

# example database 1
sudo apt-get -y install unzip
wget http://downloads.mysql.com/docs/world.sql.zip
unzip world.sql.zip
mysql -uroot -p$DB_ROOT_PASS -e "SOURCE /home/vagrant/world.sql"

# example database 2
wget https://raw.githubusercontent.com/dite-bth/ME1579-VT17/master/excercises/database/classic.sql
mysql -uroot -p$DB_ROOT_PASS -e "SOURCE /home/vagrant/classic.sql"

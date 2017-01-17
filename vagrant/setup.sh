# Change these to suit your needs...
DBHOST=localhost
DBNAME=dbname
DBUSER=dbuser
DBPASSWD=test123
DB_ROOT_PASS=password123

apt-get -y install curl build-essential python-software-properties git python3 python3-pip

debconf-set-selections <<< "mysql-server mysql-server/root_password password $DB_ROOT_PASS"
debconf-set-selections <<< "mysql-server mysql-server/root_password_again password $DB_ROOT_PASS"

apt-get -y install mysql-server

# mysql -uroot -p$DB_ROOT_PASS -e "CREATE DATABASE $DBNAME"
mysql -uroot -p$DB_ROOT_PASS -e "grant all privileges on $DBNAME.* to '$DBUSER'@'$DBHOST' identified by '$DBPASSWD'" 

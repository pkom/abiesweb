#!/bin/sh
#exportamos a sql de mysql
./mdb2mysql -d abies.mdb > abies.sql
#importamos a mysql
mysql -h mysql --default_character_set utf8 -u abies --password=abies < abies.sql

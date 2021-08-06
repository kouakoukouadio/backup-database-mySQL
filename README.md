# sauvegarde-d-une-base-de-donnée-sur-mysql-seveur(debian)


Installation d'un serveur mysql 

    sudo apt-get update 
    sudo apt-get upgrade
    sudo apt-get install mysql-server mysql-client
    sudo mysql_secure_installation

Vérifier si mysql est bien installer 

    sudo systemctl status mysql
    
Une fois que tout est ok il faut créer un user mysql avec tous les droits.

    sudo mysql -u root -p
    
Une fois accés à mysql taper la commande

    GRANT ALL ON *.* TO 'nom_user'@'localhost' IDENTIFIED BY 'user_password';
    FLUSH PRIVILEGES;
    quit

Nous pouvons  installer Apache et PHP.
   
    sudo apt-get install  apache2  php  php-json  php-mbstring  php-zip  php-gd  php-xml  php-curl php-mysql


Maintenant nous pouvons  installé Phpmyadmin

Si tout est bon taper la commande

   sudo apt-get install phpmyadmin
   
Pour vous connecter à phpmyadmin aller sur une page web puis:
    
    https://ip_du_serveur/phpmyadmin
    login-user et password-user son ceux des information de votre base de donnée  serveur-mysql.

à partir de phpmyadmin ont peut exporter  une base de donnée en format .sql.    
 

#Pour cela j'ai mis en place un script dans le but d'automatiser la sauvegarde de base de données.   

et pour cette automatisation nous allons avoir des points essentielles de notre script python que nous devrions le precisé qui sont les suivants:

-la version du script : 1.4

-tester avec : python3 sur linux 

-le nom de la base de donnée
DB_NAME = 'serv_web'

-le nom d'utilisateur  de la base de donnée
DB_USER = 'root'

-le repertoire de sauvegarde
BACKUP_PATH = '/backup/dbbackup/'

-rendre le script executable avec la commande 
chmod +x dbbackup.py

-Et executer le script comme ceci
python3 dbbackup.py

#A la fin il nous faut planifier l'execution de ce script à l'intervalle regulier  de 2 heures à l'aide de crontab
en faisant suivant ces étapes :

crontab -e

0 2 * * * /usr/bin/python3 /home/srv/backup-database-mySQL/dbbackup.py



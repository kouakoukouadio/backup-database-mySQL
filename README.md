Installation d'un serveur mysql ou mariadb

sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install mysql-server mysql-client
sudo mysql_secure_installation

Vérifier si mysql est bien installé

sudo systemctl status mysql

Une fois que tout est ok il faut créer un user mysql avec tous les droits.

sudo mysql -u root -p

Une fois accés à mariadb taper la commande

GRANT ALL ON *.* TO 'nom_user'@'localhost' IDENTIFIED BY 'user_password';
FLUSH PRIVILEGES;
quit

Nous pouvons aussi installer Phpmyadmin,mais avant il faut installer Apache et PHP.

sudo apt-get install apache2 php php-json php-mbstring php-zip php-gd php-xml php-curl php-mysql

Si tout est bon taper la commande

sudo apt-get install phpmyadmin

Pour vous connecter à phpmyadmin aller sur une page web puis:

https://ip_du_serveur/phpmyadmin

login-user et password-user son ceux de votre serveur-mysql.

A partir de phpmyadmin ont peut exporter et importer une base de donnée en format .sql.

Mises en place d'un script dans le but d'automatiser la sauvegarde de base de données.

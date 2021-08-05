#!/usr/bin/python

###########################################################
# This python script is used for mysql database backup
# using mysqldump and tar utility.
# Written by :Kouadio Kouakou Donatien
# Created date: Aout 03, 2021
# Last modified: Aout  06, 2021
# Tested with : Python 3
# Script Revision: 1.4
##########################################################

# Importation des bibliothèques de Python

import os #module permettant de manipuler les chmins de fichier
import time #module de l'heure
from  datetime import date #module de la date
import calendar

# Base de données MYSQL vers laquelle effectuer la sauvegarde

DB_HOST = 'localhost'  #Login de la machine
DB_USER = 'root'       #Login utilisateur
DB_USER_PASSWORD = 'root' #mot de passe
DB_NAME = 'serv_web' #le nom de la Database à sauvegarder
BACKUP_PATH = '/backup/dbbackup/' #Le chemin du dossier de sauvegarde

#Création du dossier de sauvegarde avec la date et l'heure actuelle "10/04/2021".
my_date= date.today()
today=calendar.day_name[my_date.weekday()]

TODAYBACKUPPATH = BACKUP_PATH + today+'/' #Le chemin du dossier et son nom

# Vérifie si le dossier de sauvegarde existe déjà, si il n'existe pas alors il le créera.

if not os.path.exists(TODAYBACKUPPATH): #vérifie le chemin du dossier
    print ("création du dossier de sauvegarde.")
    os.makedirs(TODAYBACKUPPATH)  #ici il va créer le dossier

# Vérification d'une sauvegarde de database DB_NAME.
print ("vérification des fichiers de noms de bases de données.")
if not os.path.exists(TODAYBACKUPPATH+DB_NAME+'.sql'):  #vérifie si le chemin de la bd existe
    print (TODAYBACKUPPATH+DB_NAME+'.sql',"fichier de bases de données introuvable...")
    print ("démarrage de la sauvegarde complète de la base de données" + DB_NAME)
    multi = 0
else:
    file1 = open(TODAYBACKUPPATH+DB_NAME+'.sql')
    multi = 1
    print ("fichier de bases de données trouvé...")
    print ("démarrage de la sauvegarde incrémentale de la bases de données répertoriées dans le fichier " + DB_NAME)


# Démarrage du processus de sauvegarde de la base de données réelle.
if multi:
   in_file = open(TODAYBACKUPPATH+DB_NAME+'.sql',"r")
   flength = len(in_file.readlines())
   in_file.close()
   p = 1
   dbfile = open(TODAYBACKUPPATH+DB_NAME+".sql" ,"r")

   while p <= flength:
       db = dbfile.readline()   # lecture du nom de la base de données à partir du fichier
       db = db[:-1]         # supprimer une ligne supplémentaire
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + DB_NAME + " > " + TODAYBACKUPPATH +DB_NAME + ".sql" #ici mysqldump permet d'exporter la bd.
       os.system(dumpcmd)
       p = p + 1
   dbfile.close()
else:
   db = DB_NAME
   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db +".sql"
   os.system(dumpcmd)

print ("script de sauvegarde terminé")
print ("Vos sauvegardes ont été créées dans le repertoire '" + TODAYBACKUPPATH + "' annuaire")

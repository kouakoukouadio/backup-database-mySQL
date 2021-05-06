# Importation des bibliothèques de Python 
import os #module permettant de manipuler les chmins de fichier
import time #module de l'heure
import datetime #module de la date
 
# Base de données MYSQL vers laquelle effectuer la sauvegarde 
 
DB_HOST = 'localhost'  #Login de la machine
DB_USER = 'root'       #Login utilisateur
DB_USER_PASSWORD = 'root' #mot de passe
DB_NAME = 'serv_web' #le nom de la Database à sauvegarder
BACKUP_PATH = '/backup/dbbackup/' #Le chemin du dossier de sauvegarde 
 
#Création du dossier de sauvegarde avec la date et l'heure actuelle "10/04/2021-12:48". 
DATETIME = time.strftime('%d/%m/%Y-%H:%M') #le nom du dossier de sauvegarde
 
TODAYBACKUPPATH = BACKUP_PATH + DATETIME #Le chemin du dossier et son nom
 
# Vérifie si le dossier de sauvegarde existe déjà, si il n'existe pas alors il le créera. 
print ("création du dossier de sauvegarde.") 
if not os.path.exists(TODAYBACKUPPATH): #vérifie le chemin du dossier 
    os.makedirs(TODAYBACKUPPATH)  #ici il va créer le dossier
 
# Vérification d'une sauvegarde de database DB_NAME. 
print ("vérification des fichiers de noms de bases de données.") 
if os.path.exists(DB_NAME):  #vérifie si le chemin de la bd existe
    file1 = open(DB_NAME) 
    multi = 1 
    print ("fichier de bases de données trouvé...") 
    print ("démarrage de la sauvegarde de la bases de données répertoriées dans le fichier ") + DB_NAME 
else: 
    print ("fichier de bases de données introuvable...") 
    print ("démarrage de la sauvegarde de la base de données" + DB_NAME) 
    multi = 0 
 
# Démarrage du processus de sauvegarde de la base de données réelle. 
if multi: 
   in_file = open(DB_NAME,"r") 
   flength = len(in_file.readlines()) 
   in_file.close() 
   p = 1 
   dbfile = open(DB_NAME,"r") 
 
   while p <= flength: 
       db = dbfile.readline()   # lecture du nom de la base de données à partir du fichier
       db = db[:-1]         # supprimer une ligne supplémentaire 
       dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql" #ici mysqldump permet d'exporter la bd.
       os.system(dumpcmd) 
       p = p + 1 
   dbfile.close() 
else: 
   db = DB_NAME 
   dumpcmd = "mysqldump -u " + DB_USER + " -p" + DB_USER_PASSWORD + " " + db + " > " + TODAYBACKUPPATH + "/" + db + ".sql" 
   os.system(dumpcmd) 
 
print ("script de sauvegarde terminé") 
print ("Vos sauvegardes ont été créées dans le repertoire '" + TODAYBACKUPPATH + "' annuaire") 

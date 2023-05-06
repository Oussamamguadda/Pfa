import mysql.connector
from mysql.connector import Error
####
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QDialog, QApplication, QMessageBox
#from ..signup import *
####

class Compte:

    def __init__(self, nom_utilisateur, mdp):
        self.nom_utilisateur = nom_utilisateur
        self.mdp = mdp
        self.mydb = mysql.connector.connect(
                                        host='localhost',
                                           database='pfa',
                                           user='root',
                                           password='')
        self.cur=self.mydb.cursor()
        

     # Méthode pour vérifier si le compte existe dans la base de données MySQL
    def verifier_compte(self):
        # Connexion à la base de données
        try:
            

        # Exécution de la requête SQL pour récupérer le compte correspondant au nom d'utilisateur et au mot de passe
            sql = "SELECT * FROM manager WHERE login = %s AND password = %s"
            val = (self.nom_utilisateur, self.mdp)
            self.cur.execute(sql, val)
        
            # Vérification du résultat de la requête
            result = self.cur.fetchone()
            if result:
                return True  # le compte existe dans la base de données
            else:
                return False  # le compte n'existe pas dans la base de données
        except:
            print("error")
    

    
    # def ajouter(self):
        
    #     ## verifier si le compte est deja existe
    #     compte = Compte( self.nom_utilisateur,self.mdp)
    #     ct_v=compte.verifier_compte()
        
    #     if ct_v==True:
    #         return 0
    #     else:
    #         try:
    #             self.cur.execute("INSERT INTO compte (USERNAME, PASSWORD) VALUES (%s, %s)", 
    #                        (self.nom_utilisateur, self.mdp))
    #             self.mydb.commit()
    #             return 1
    #         except Error as e:
    #             print(e)
    #             return None
    #         finally:
    #             self.cur.close()
    #             self.cur.close()


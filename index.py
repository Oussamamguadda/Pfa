import sys
import re
from typing import Self
from PyQt5.uic import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sqlite3
from PyQt5.QtWidgets import (QApplication, QWidget, QFileDialog, QTextEdit, QPushButton, QLabel, QVBoxLayout, QMessageBox,QMainWindow)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QDir
import platform
from PyQt5 import QtCore, QtGui,  QtWidgets
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient,QPen)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QByteArray
import hashlib
from login import Ui_MainWindow
from signUp import Ui_MainWindow
from voiture import Ui_MainWindow
from client import Ui_MainWindow
from home import Ui_MainWindow


class client(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        super(client,self).__init__()
        loadUi("client.ui",self)
        self.btnajouter.clicked.connect(self.ajouterclient)
        self.deletebtn.clicked.connect(self.delete)
        self.btnrefresh.clicked.connect(self.getdata) 
        self.btnretour.clicked.connect(self.retour)
    def ajouterclient(self):
        email = self.emailfield.text()
        nom = self.nomfield.text()
        prenom = self.prenomfield.text()
        telephone = self.telephonefield.text()
        # Function to validate email
        def validate_email(email):
            pattern = r'^[\w-]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$'
            if re.match(pattern, email):
                return True
            else:
                return False

# Function to validate telephone number
        def validate_phone(telephone):
            pattern = r'^\d{10}$'
            if re.match(pattern, telephone):
                return True
            else:
                return False   
        if len(email)==0 or len(nom)==0 or len(prenom)==0 or len(telephone)==0 :
                
                QMessageBox.warning(self,'Message','Fill in all fields')

            
        elif validate_email(email)==False:
            
            
            QMessageBox.information(self,'Message','fill in the mails field like exemple@exemple.exemple')
         

        elif validate_phone(telephone)==False:
            QMessageBox.information(self,'Message','Please enter a valid 10-digit phone number')
            

        else:
            
            conn = sqlite3.connect("database1.db")
            cur = conn.cursor()
            user_info = [ email ,nom,prenom,telephone]
            query = 'INSERT INTO customer Values(null,?,?,?,?)'
            cur.execute(query, user_info)
            QMessageBox.information(self,'Message','successfully added ',QMessageBox.Ok)

            
            conn.commit()
            conn.close()
            
            
    
            
    
    def getdata(self):
        connection = sqlite3.connect("database1.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM customer")
        customer = cursor.fetchall()
        self.tableWidget.setRowCount(len(customer))
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Email", "Nom", "Prenom", "Telephone"])

        for row, data in enumerate(customer):
            for col, value in enumerate(data):
                if col == 8:  # column for the image
                    image_path = value.encode('utf-8').decode('utf-8') # Convert the bytes to a string
                    pixmap = QPixmap(image_path)
                    label = QLabel()
                    label.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))  # you can adjust the size as needed
                    self.tableWidget.setCellWidget(row, col, label)
                else:
                    cell = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, cell)

        cursor.close()
    def retour(self):
        home=Accueil()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def delete(self):
        def check_id_exists(id):
            connection = sqlite3.connect("database1.db")
            cursor = connection.cursor()
        
            cursor.execute("SELECT id_customer FROM customer WHERE id_customer = ?", (id,))
            row = cursor.fetchone()
            cursor.close()
        
            return row is not None
        id = self.deletefield.text()
        if not check_id_exists(id):
            QMessageBox.warning(self, "Confirmation", "client n'existe pas ")
        elif id:
            
            connection = sqlite3.connect('database1.db')
            cursor = connection.cursor()
            delete_query = 'DELETE FROM customer WHERE id_customer = ?'
            cursor.execute(delete_query, (id,))
            connection.commit()
            connection.close()
            '''self.showAllProducts()'''
            self.deletefield.setText("")
            QMessageBox.information(self, "Success", "car deleted successfully.")
        
        else:
            
            QMessageBox.warning(self, "Error", "Please select a car to delete to delete.")
    
class voiture(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        super(voiture,self).__init__()
        loadUi("voiture.ui",self)
        self.deletebtn.clicked.connect(self.delete)
        self.retourbtn.clicked.connect(self.retour)
        self.searchbtn.clicked.connect(self.search)
        self.uploadpic.clicked.connect(self.upload)
        self.btnajouter.clicked.connect(self.ajoutervoiture)
        self.btnrefresh.clicked.connect(self.getdata)
    def ajoutervoiture(self):
        
        marque = self.marquefield.text()
        modele = self.modelefield.text()
        type = self.typefield.text()
        nbr= self.nbrfield.text()
        trans = self.transcmb.currentText()
        prix = self.prixfield.text()  
        dispo = self.discmb.currentText()
        picture = self.label_3.text()
        if len(marque)==0 or len(modele)==0 or len(type)==0 or len(nbr)==0 or len (trans)==0 or len(prix)==0 or len(dispo)==0 or len(picture)==0:
                self.error1.setText("please fill in the marque's field !! ")
                self.error2.setText("please fill in the modele's field !! ")
                self.error3.setText("please fill in the type fr carburant's field !! ")
                self.error4.setText("please fill in the nombre de place's field !! ")
                self.error5.setText("please fill in the price's field !! ")
                '''self.error.setText("please fill in 's field !! ")'''
         

        else:
            
            conn = sqlite3.connect("database1.db")
            cur = conn.cursor()
            user_info = [marque,modele, type, nbr,trans,prix,dispo,picture]
            query = 'INSERT INTO voiture Values(null,?,?,?,?,?,?,?,?)'
            cur.execute(query, user_info)
            self.error1.setText("")
            self.error2.setText("")
            self.error3.setText("")
            self.error4.setText("")
            self.error5.setText("")
            self.error2.setText("")
            self.error.setText("successfully added")
            conn.commit()
            conn.close()
            self.error.setText("")
            RES= QMessageBox.information(self,'Message','Product added successfully',QMessageBox.Yes)
    def upload(self):
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open Image File', r"<Default dir>", "Image files (*.jpg *.jpeg *.gif)")
        '''print(file_name(0))'''
        self.picture_2.setPixmap(QPixmap(file_name).scaledToWidth(200))
        self.label_3.setText(file_name,) 
        with open(file_name, 'rb') as file:
            blob_data = file.read()
        sqlite3.Binary(blob_data)

    def retour(self):
        home=Accueil()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def getdata(self):
        connection = sqlite3.connect("database1.db")
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM voiture")
        voiture = cursor.fetchall()
        self.tableWidget.setRowCount(len(voiture))
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["Matricule", "marque", "modele", "typeCarburant", "nombrePlace", "Transmission", "Prix de location par jour", "disponibilite", "Image"])

        for row, data in enumerate(voiture):
            for col, value in enumerate(data):
                if col == 8:  # column for the image
                    image_path = value.encode('utf-8').decode('utf-8') # Convert the bytes to a string
                    pixmap = QPixmap(image_path)
                    label = QLabel()
                    label.setPixmap(pixmap.scaled(100, 100, QtCore.Qt.KeepAspectRatio))  # you can adjust the size as needed
                    self.tableWidget.setCellWidget(row, col, label)
                else:
                    cell = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, cell)

        cursor.close()


    def delete(self):
        
        mat = self.deletefield.text()
        if mat:
            
            connection = sqlite3.connect('database1.db')
            cursor = connection.cursor()
            delete_query = 'DELETE FROM voiture WHERE matricule = ?'
            cursor.execute(delete_query, (mat,))
            connection.commit()
            connection.close()
            '''self.showAllProducts()'''
            self.deletefield.setText("")
            QMessageBox.information(self, "Success", "car deleted successfully.")
        
        else:
            
            QMessageBox.warning(self, "Error", "Please select a car to delete to delete.")
    


        
    def search(self):
        # Get search term and search option from GUI
        search_term = self.searchfield.text()
        search_option = self.comboBox.currentText()
        
        # Connect to SQLite database
        conn = sqlite3.connect('database1.db')
        c = conn.cursor()
        
        # Execute SELECT statement based on search option
        if search_option == 'Marque':
            c.execute('SELECT * FROM voiture WHERE marque LIKE ?', ('%' + search_term + '%',))
        elif search_option == 'Type de carburant':
            c.execute('SELECT * FROM voiture WHERE typeCarburant LIKE ?', ('%' + search_term + '%',))
        elif search_option == 'Nombre de place':
            c.execute('SELECT * FROM voiture WHERE nombrePlace LIKE ?', ('%' + search_term + '%',))
        elif search_option == 'Transmission':
            # Convert search term to datetime object
            
            c.execute('SELECT * FROM voiture WHERE transmission LIKE ?', ('%' + search_term + '%',))
        elif search_option == 'Prix de location par jour':
            # Convert search term to datetime object
            
            c.execute('SELECT * FROM voiture WHERE prixLocationJour LIKE ?', ('%' + search_term + '%',))
        # Get search results and display in table wmatget
        rows = c.fetchall()
        self.tableWidget.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(i, j, item)
        
        # Close database connection
        conn.close()
class Accueil(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        super(Accueil,self).__init__()
        loadUi("home.ui",self)
        self.voitureBtn.clicked.connect(self.gotovoiture)
        self.clientbtn.clicked.connect(self.gotoclient)
    def gotovoiture(self):
        home=voiture()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def gotoclient(self):
        home=client()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
class login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        super(login,self).__init__()
        loadUi("login.ui",self)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.btnSignup.clicked.connect(self.gotocreateacc)
        self.passInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton.clicked.connect(self.loginfunction)
        '''self.quitter.clicked.connect(app.quit)'''
        
    def gotocreateacc(QDialog):
        createacc=Signup()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def loginfunction(self):
        user = self.userInput.text()
        password = self.passInput.text()
        username_hashed = hashlib.sha256(user.encode()).hexdigest()
        password_hashed = hashlib.sha256(password.encode()).hexdigest()
        if len(username_hashed)==0 or len(password_hashed)==0:
            self.error.setText("please fill in ALL the fields !! ")
        else:
            conn = sqlite3.connect("database1.db")
            cur = conn.cursor()
            query = 'SELECT password FROM client WHERE login =\''+username_hashed+"\'"
            cur.execute(query)
            result_pass = cur.fetchone()
        if result_pass is not None and result_pass[0] == password_hashed : 
            print("Successfully logged in .")
            self.error.setText("")
            window=Accueil()
            widget.addWidget(window)
            widget.setCurrentIndex(widget.currentIndex()+1)
            window.setWindowTitle('Login')
            window.setWindowIcon(QIcon('ic.png'))
            RES= QMessageBox.information(window,'Message','Login successfully',QMessageBox.Yes)
        else:
            self.error.setText("Invalid username or password.")
            QMessageBox.warning(self, "Error", "Invalid username or password.")

class Signup(QMainWindow):
    def __init__(self):
        def __init__(self):
            QMainWindow.__init__(self)
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

        super(Signup,self).__init__()
        loadUi("signUp.ui",self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.C_passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btn_signup.clicked.connect(self.signupfunction)
        self.pushButton_9.clicked.connect(self.home)
        
    def home(self):
        home=login()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
    

    def signupfunction(self):
        
        
        user = self.usernamefield.text()
        firstname = self.first_namefield.text()
        lastname = self.last_namefield.text()
        password = self.passwordfield.text()
        cpassword = self.C_passwordfield.text()  
        username_hashed = hashlib.sha256(user.encode()).hexdigest()
        password_hashed = hashlib.sha256(password.encode()).hexdigest()
        cpassword_hashed = hashlib.sha256(cpassword.encode()).hexdigest()
           
        if len(username_hashed)==0 or len(firstname)==0 or len(lastname)==0  or len (password_hashed)==0 or len(cpassword_hashed)==0 :
                self.error1.setText("please fill in the username's field !! ")
                self.error2.setText("please fill in the firstname's field !! ")
                self.error3.setText("please fill in the lastname's field !! ")
                self.error5.setText("please fill in the password's field !! ")
                self.error6.setText("please fill in the confirm password's field !! ")
        elif password_hashed != cpassword_hashed:
            self.error.setText("password and confirm password did not match !!!")
            
        else:
            
            conn = sqlite3.connect("database1.db")
            cur = conn.cursor()
            user_info = [ username_hashed, password_hashed, cpassword_hashed,firstname,lastname]
            query = 'INSERT INTO client Values(null,?,?,?,?,?)'
            cur.execute(query, user_info)
            self.error1.setText("")
            self.error2.setText("")
            self.error3.setText("")
            self.error5.setText("")
            self.error6.setText("")
            self.error.setText("successfully signed up")
            conn.commit()
            conn.close()
            self.error.setText("")
            
            Login=login()
            widget.addWidget(Login)
            widget.setCurrentIndex(widget.currentIndex()+1)
            Login.setWindowTitle('login')
            Login.setWindowIcon(QIcon('ic.png'))
            RES= QMessageBox.information(Login,'Message','Successfully Signed Up',QMessageBox.Yes)
            
    



app =QApplication(sys.argv)
welcome=login()
widget = QtWidgets.QStackedWidget()

widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()


try:
    sys.exit(app.exec_())
except:
    print("Exiting")



    
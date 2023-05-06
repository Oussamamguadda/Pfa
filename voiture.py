# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'voiture.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 655)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QLineEdit{\n"
"    height:30px;\n"
"    padding-left:5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    height:30px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.picture = QtWidgets.QWidget(self.widget)
        self.picture.setGeometry(QtCore.QRect(-1, -1, 341, 631))
        self.picture.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.picture.setObjectName("picture")
        self.modelefield = QtWidgets.QLineEdit(self.picture)
        self.modelefield.setGeometry(QtCore.QRect(20, 70, 211, 31))
        self.modelefield.setStyleSheet("background:transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border:none;\n"
"color:#ffffff;\n"
"border-bottom:1px solid #ffffff;\n"
"")
        self.modelefield.setObjectName("modelefield")
        self.nbrfield = QtWidgets.QLineEdit(self.picture)
        self.nbrfield.setGeometry(QtCore.QRect(20, 190, 211, 31))
        self.nbrfield.setStyleSheet("background:transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border:none;\n"
"color:#ffffff;\n"
"border-bottom:1px solid #ffffff;\n"
"")
        self.nbrfield.setObjectName("nbrfield")
        self.typefield = QtWidgets.QLineEdit(self.picture)
        self.typefield.setGeometry(QtCore.QRect(20, 130, 211, 31))
        self.typefield.setStyleSheet("background:transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border:none;\n"
"color:#ffffff;\n"
"border-bottom:1px solid #ffffff;\n"
"")
        self.typefield.setObjectName("typefield")
        self.prixfield = QtWidgets.QLineEdit(self.picture)
        self.prixfield.setGeometry(QtCore.QRect(30, 320, 211, 31))
        self.prixfield.setStyleSheet("background:transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border:none;\n"
"color:#ffffff;\n"
"border-bottom:1px solid #ffffff;\n"
"")
        self.prixfield.setObjectName("prixfield")
        self.picture_2 = QtWidgets.QLabel(self.picture)
        self.picture_2.setGeometry(QtCore.QRect(40, 450, 171, 121))
        self.picture_2.setObjectName("picture_2")
        self.uploadpic = QtWidgets.QPushButton(self.picture)
        self.uploadpic.setGeometry(QtCore.QRect(220, 480, 101, 24))
        self.uploadpic.setObjectName("uploadpic")
        self.btnajouter = QtWidgets.QPushButton(self.picture)
        self.btnajouter.setGeometry(QtCore.QRect(90, 580, 141, 24))
        self.btnajouter.setObjectName("btnajouter")
        self.label_3 = QtWidgets.QLabel(self.picture)
        self.label_3.setGeometry(QtCore.QRect(250, 530, 49, 16))
        self.label_3.setObjectName("label_3")
        self.transcmb = QtWidgets.QComboBox(self.picture)
        self.transcmb.setGeometry(QtCore.QRect(30, 250, 201, 31))
        self.transcmb.setObjectName("transcmb")
        self.transcmb.addItem("")
        self.transcmb.addItem("")
        self.discmb = QtWidgets.QComboBox(self.picture)
        self.discmb.setGeometry(QtCore.QRect(30, 380, 211, 31))
        self.discmb.setObjectName("discmb")
        self.discmb.addItem("")
        self.discmb.addItem("")
        self.error1 = QtWidgets.QLabel(self.picture)
        self.error1.setGeometry(QtCore.QRect(20, 60, 221, 16))
        self.error1.setObjectName("error1")
        self.error2 = QtWidgets.QLabel(self.picture)
        self.error2.setGeometry(QtCore.QRect(10, 110, 221, 16))
        self.error2.setObjectName("error2")
        self.error3 = QtWidgets.QLabel(self.picture)
        self.error3.setGeometry(QtCore.QRect(10, 170, 221, 16))
        self.error3.setObjectName("error3")
        self.error4 = QtWidgets.QLabel(self.picture)
        self.error4.setGeometry(QtCore.QRect(10, 230, 221, 16))
        self.error4.setObjectName("error4")
        self.error5 = QtWidgets.QLabel(self.picture)
        self.error5.setGeometry(QtCore.QRect(10, 360, 221, 16))
        self.error5.setObjectName("error5")
        self.error = QtWidgets.QLabel(self.picture)
        self.error.setGeometry(QtCore.QRect(30, 610, 221, 16))
        self.error.setObjectName("error")
        self.marquefield = QtWidgets.QLineEdit(self.picture)
        self.marquefield.setGeometry(QtCore.QRect(20, 20, 211, 31))
        self.marquefield.setStyleSheet("background:transparent;\n"
"border-color: rgb(255, 255, 255);\n"
"border:none;\n"
"color:#ffffff;\n"
"border-bottom:1px solid #ffffff;\n"
"")
        self.marquefield.setInputMask("")
        self.marquefield.setObjectName("marquefield")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(340, 80, 431, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(540, 10, 171, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.searchbtn = QtWidgets.QPushButton(self.widget)
        self.searchbtn.setGeometry(QtCore.QRect(360, 40, 111, 31))
        self.searchbtn.setObjectName("searchbtn")
        self.searchfield = QtWidgets.QLineEdit(self.widget)
        self.searchfield.setGeometry(QtCore.QRect(360, 10, 171, 31))
        self.searchfield.setObjectName("searchfield")
        self.deletebtn = QtWidgets.QPushButton(self.widget)
        self.deletebtn.setGeometry(QtCore.QRect(590, 370, 171, 31))
        self.deletebtn.setObjectName("deletebtn")
        self.retourbtn = QtWidgets.QPushButton(self.widget)
        self.retourbtn.setGeometry(QtCore.QRect(730, 10, 75, 24))
        self.retourbtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-flèche-gauche-52.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.retourbtn.setIcon(icon)
        self.retourbtn.setObjectName("retourbtn")
        self.btnrefresh = QtWidgets.QPushButton(self.widget)
        self.btnrefresh.setGeometry(QtCore.QRect(360, 310, 121, 41))
        self.btnrefresh.setObjectName("btnrefresh")
        self.deletefield = QtWidgets.QLineEdit(self.widget)
        self.deletefield.setGeometry(QtCore.QRect(350, 370, 221, 31))
        self.deletefield.setObjectName("deletefield")
        self.horizontalLayout.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.modelefield.setText(_translate("MainWindow", "modele"))
        self.nbrfield.setText(_translate("MainWindow", "nombre de place"))
        self.typefield.setText(_translate("MainWindow", "Type du carburant"))
        self.prixfield.setText(_translate("MainWindow", "prix de location par jour"))
        self.picture_2.setText(_translate("MainWindow", "image"))
        self.uploadpic.setText(_translate("MainWindow", "upload picture"))
        self.btnajouter.setText(_translate("MainWindow", "ajouter"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.transcmb.setCurrentText(_translate("MainWindow", "Automatique"))
        self.transcmb.setItemText(0, _translate("MainWindow", "Automatique"))
        self.transcmb.setItemText(1, _translate("MainWindow", "manuelle"))
        self.discmb.setItemText(0, _translate("MainWindow", "disponible"))
        self.discmb.setItemText(1, _translate("MainWindow", "non disponilbe"))
        self.error1.setText(_translate("MainWindow", "TextLabel"))
        self.error2.setText(_translate("MainWindow", "TextLabel"))
        self.error3.setText(_translate("MainWindow", "TextLabel"))
        self.error4.setText(_translate("MainWindow", "TextLabel"))
        self.error5.setText(_translate("MainWindow", "TextLabel"))
        self.error.setText(_translate("MainWindow", "TextLabel"))
        self.marquefield.setText(_translate("MainWindow", "marque"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Marque"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Type de carburant"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Nombre de place"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Transmission"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Prix de location par jour"))
        self.searchbtn.setText(_translate("MainWindow", "search"))
        self.deletebtn.setText(_translate("MainWindow", "delete"))
        self.btnrefresh.setText(_translate("MainWindow", "refresh"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
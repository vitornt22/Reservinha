# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Esqueceusenha.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from cliente import cliente
from verificaEmail import verificaEmail, verificaCpf, verificaTelefone, verificaMat
import smtplib
from random import randint
class Ui_Senha(object):
    def setupUi(self, MainWindow):
        self.codigo = 0
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-37, -4, 781, 481))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../fundo azul.jpg"))
        self.label_2.setObjectName("label_2")
        self.Email = QtWidgets.QLineEdit(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(170, 110, 301, 41))
        self.Email.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.Email.setText("")
        self.Email.setObjectName("Email")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 120, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 260, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 250, 301, 41))
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 220, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.Nova_senha = QtWidgets.QLineEdit(self.centralwidget)
        
        self.Nova_senha.setGeometry(QtCore.QRect(170, 200, 301, 41))
        self.Nova_senha.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.Nova_senha.setText("")
        self.Nova_senha.setObjectName("Nova_senha")
        self.redef = QtWidgets.QPushButton(self.centralwidget)
        self.redef.setGeometry(QtCore.QRect(130, 310, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.redef.setFont(font)
        self.redef.setObjectName("redef")
        self.codigo = QtWidgets.QPushButton(self.centralwidget)
        self.codigo.setGeometry(QtCore.QRect(340, 310, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.codigo.setFont(font)
        self.codigo.setObjectName("codigo")
        self.codigo_2 = QtWidgets.QPushButton(self.centralwidget)
        self.codigo_2.setGeometry(QtCore.QRect(230, 160, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.codigo_2.setFont(font)
        self.codigo_2.setObjectName("codigo_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "EMAIL"))
        self.label_4.setText(_translate("MainWindow", "NOVA SENHA"))
        self.label_5.setText(_translate("MainWindow", "CÓDIGO"))
        self.redef.setText(_translate("MainWindow", "Redefinir Senha"))
        self.codigo.setText(_translate("MainWindow", "Voltar"))
        self.codigo_2.setText(_translate("MainWindow", "Enviar código"))
        self.funcionalidade()
        
    def funcionalidade(self):
        self.codigo_2.clicked.connect(self.envia_codigo)
        
        self.redef.clicked.connect(self.altera_senha)
    def envia_codigo(self):
        self.email = self.Email.text()
        dados = "envia"+","+self.email
        print(dados)
        
        c1 = cliente(dados)
        if(c1.client_socket.recv(1024).decode()=="exist"):
            codigo = randint(100000,999999)
            self.codigo = str(codigo)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login("reservadossantos9@gmail.com", "euconsigo123")
            server.sendmail("reservadossantos9@gmail.com",self.email, str(codigo))
            QtWidgets.QMessageBox.about(None, "AVISO","CODIGO ENVIADO VERFIQUE O EMAIL",)

        else:
            QtWidgets.QMessageBox.about(None, "AVISO","EMAIL NÃO CADASTRADO!",)

    def altera_senha(self):
       
        
        
        
        if(self.codigo==self.Nova_senha.text() and  len(self.lineEdit_3.text())>1):
           dados = "verifica"+","+self.email+","+self.lineEdit_3.text()
           print(dados)
           c1 = cliente(dados)
           
           
           QtWidgets.QMessageBox.about(None, "AVISO","Senha redefinida com sucesso!",)     
           self.lineEdit_3.clear()
           self.Email.clear()
           self.Nova_senha.clear()
                 
           
        else:
            QtWidgets.QMessageBox.about(None, "AVISO","Senha invalida ou codigo invalido",)
            
            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Esq_Senha = QtWidgets.QMainWindow()
    ui = Ui_Senha()
    ui.setupUi(Esq_Senha)
    Esq_Senha.show()
    sys.exit(app.exec_())

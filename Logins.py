# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Logins.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        self.verifica = 0
        Login.setObjectName("Login")
        Login.resize(760, 457)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    background-color : white;\n"
"\n"
"}\n"
"\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.FundoAzul = QtWidgets.QLabel(self.centralwidget)
        self.FundoAzul.setGeometry(QtCore.QRect(-40, -20, 851, 461))
        self.FundoAzul.setText("")
        self.FundoAzul.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.FundoAzul.setScaledContents(True)
        self.FundoAzul.setObjectName("FundoAzul")
        self.sair = QtWidgets.QPushButton(self.centralwidget)
        self.sair.setGeometry(QtCore.QRect(410, 250, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sair.setFont(font)
        self.sair.setStyleSheet("QPushButton{\n"
"    background-color: royalblue;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"\n"
"}")
        self.sair.setObjectName("sair")
        self.Email = QtWidgets.QLabel(self.centralwidget)
        self.Email.setGeometry(QtCore.QRect(140, 130, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Email.setFont(font)
        self.Email.setStyleSheet("QLabel{\n"
"    color: blue;\n"
"    background-color: rgba(0, 0, 0,0);\n"
"\n"
"\n"
"}")
        self.Email.setObjectName("Email")
        self.EsqueceuSenha = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.EsqueceuSenha.setGeometry(QtCore.QRect(220, 210, 168, 41))
        self.EsqueceuSenha.setStyleSheet("QCommandLinkButton{\n"
"    color: rgb(0, 85, 255)\n"
"    \n"
"    \n"
"}")
        self.EsqueceuSenha.setObjectName("EsqueceuSenha")
        self.entrar = QtWidgets.QPushButton(self.centralwidget)
        self.entrar.setGeometry(QtCore.QRect(220, 250, 91, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.entrar.setFont(font)
        self.entrar.setStyleSheet("QPushButton{\n"
"    background-color: royalblue;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:white;\n"
"}")
        self.entrar.setObjectName("entrar")
        self.Senha = QtWidgets.QLabel(self.centralwidget)
        self.Senha.setGeometry(QtCore.QRect(140, 180, 59, 18))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Senha.setFont(font)
        self.Senha.setStyleSheet("QLabel{\n"
"    color: blue;\n"
"    background-color: rgba(0, 0, 0,0);\n"
"\n"
"}")
        self.Senha.setObjectName("Senha")
        self.CampoEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.CampoEmail.setGeometry(QtCore.QRect(220, 130, 281, 29))
        self.CampoEmail.setObjectName("CampoEmail")
        self.CampoSenha = QtWidgets.QLineEdit(self.centralwidget)
        self.CampoSenha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CampoSenha.setGeometry(QtCore.QRect(220, 180, 281, 29))
        self.CampoSenha.setObjectName("CampoSenha")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(270, 30, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Noto Color Emoji")
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("QLabel{\n"
"    color: rgb(85, 0, 255);\n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.Titulo.setObjectName("Titulo")
        self.LogoUfpi = QtWidgets.QLabel(self.centralwidget)
        self.LogoUfpi.setGeometry(QtCore.QRect(-20, 320, 150, 100))
        self.LogoUfpi.setStyleSheet("QLabel{\n"
"    background-color: rgba(0,0,0,0);\n"
"}")
        self.LogoUfpi.setText("")
        self.LogoUfpi.setPixmap(QtGui.QPixmap("../../../../ufpi.png"))
        self.LogoUfpi.setScaledContents(True)
        self.LogoUfpi.setObjectName("LogoUfpi")
        Login.setCentralWidget(self.centralwidget)
        self.rodape = QtWidgets.QToolBar(Login)
        self.rodape.setObjectName("rodape")
        Login.addToolBar(QtCore.Qt.TopToolBarArea, self.rodape)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "MainWindow"))
        self.sair.setText(_translate("Login", "SAIR"))
        self.Email.setText(_translate("Login", "EMAIL"))
        self.EsqueceuSenha.setText(_translate("Login", "Esqueceu senha?"))
        self.entrar.setText(_translate("Login", "ENTRAR"))
        self.Senha.setText(_translate("Login", "SENHA"))
        self.Titulo.setText(_translate("Login", "LOGIN"))
        self.rodape.setWindowTitle(_translate("Login", "toolBar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())


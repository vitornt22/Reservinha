# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logarComo.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Logins import Ui_Login
from TelaCoordenador import Ui_MenuCoordenador
from TelaProfessor import Ui_MenuProfessor
from TelaMonitor import Ui_MenuMonitor
from TelaTecnico import Ui_MenuTecnico
from AlterarEmail import Ui_AlterarEMAIL
from AlterarTelefone import Ui_AlterarTELEFONE

from redefinirSenha import Ui_RedefinirSenha
from cliente import cliente


import sys


class Ui_inicio(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(681, 444)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fundoazul = QtWidgets.QLabel(self.centralwidget)
        self.fundoazul.setGeometry(QtCore.QRect(-100, -50, 791, 531))
        self.fundoazul.setText("")
        self.fundoazul.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundoazul.setObjectName("fundoazul")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(240, 40, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 90, 251, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.AgrupamentodeLines = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.AgrupamentodeLines.setContentsMargins(0, 0, 0, 0)
        self.AgrupamentodeLines.setObjectName("AgrupamentodeLines")
        self.Botaoprofessor = QtWidgets.QPushButton(self.layoutWidget)
        self.Botaoprofessor.setObjectName("Botaoprofessor")
        self.AgrupamentodeLines.addWidget(self.Botaoprofessor)
        self.BotaoMonitor = QtWidgets.QPushButton(self.layoutWidget)
        self.BotaoMonitor.setObjectName("BotaoMonitor")
        self.AgrupamentodeLines.addWidget(self.BotaoMonitor)
        self.Botaocoordenador = QtWidgets.QPushButton(self.layoutWidget)
        self.Botaocoordenador.setObjectName("Botaocoordenador")
        self.AgrupamentodeLines.addWidget(self.Botaocoordenador)
        self.Botaocoordenador_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.Botaocoordenador_2.setObjectName("Botaocoordenador_2")
        self.AgrupamentodeLines.addWidget(self.Botaocoordenador_2)
        self.Botaocoordenador_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.Botaocoordenador_3.setObjectName("Botaocoordenador_3")
        self.AgrupamentodeLines.addWidget(self.Botaocoordenador_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.rodape = QtWidgets.QStatusBar(MainWindow)
        self.rodape.setObjectName("rodape")
        MainWindow.setStatusBar(self.rodape)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titulo.setText(_translate("MainWindow", "Entrar como"))
        self.Botaoprofessor.setText(_translate("MainWindow", "Professor"))
        self.BotaoMonitor.setText(_translate("MainWindow", "Monitor"))
        self.Botaocoordenador.setText(_translate("MainWindow", "Coordenador"))
        self.Botaocoordenador_2.setText(_translate("MainWindow", "Tecnico"))
        self.Botaocoordenador_3.setText(_translate("MainWindow", "Sair do programa"))


class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
            

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.stack8 = QtWidgets.QMainWindow()
            
            
        self.tela_inicio = Ui_inicio()
        self.tela_login = Ui_Login()
        self.tela_coordenador = Ui_MenuCoordenador()
        self.tela_professor = Ui_MenuProfessor()
        self.tela_monitor = Ui_MenuMonitor()
        self.tela_tecnico = Ui_MenuTecnico()
        self.tela_alterar_email = Ui_AlterarEMAIL()
        self.tela_alterar_telefone = Ui_AlterarTELEFONE()
        self.tela_alterar_senha = Ui_RedefinirSenha()

        
        self.tela_inicio.setupUi(self.stack0)
        self.tela_login.setupUi(self.stack1)
        self.tela_coordenador.setupUi(self.stack2,None)
        self.tela_professor.setupUi(self.stack3,None)
        self.tela_monitor.setupUi(self.stack4)
        self.tela_tecnico.setupUi(self.stack5,None)        
        self.tela_alterar_email.setupUi(self.stack6)
        self.tela_alterar_telefone.setupUi(self.stack7)
        self.tela_alterar_senha.setupUi(self.stack8)
        
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        



class Main(QtWidgets.QMainWindow,Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.tela_inicio.BotaoMonitor.clicked.connect(self.entrar_monit)
        self.tela_inicio.Botaoprofessor.clicked.connect(self.entrar_prof)
        self.tela_inicio.Botaocoordenador.clicked.connect(self.entrar_coord)
        self.tela_inicio.Botaocoordenador_2.clicked.connect(self.entrar_tec)
        self.tela_login.sair.clicked.connect(self.voltar)
        self.tela_login.entrar.clicked.connect(self.logando)
        
        self.tela_tecnico.cancelar.clicked.connect(self.cancelar)
        self.tela_professor.cancelar.clicked.connect(self.cancelar)
        self.tela_coordenador.cancelar.clicked.connect(self.cancelar)
        self.tela_inicio.Botaocoordenador_3.clicked.connect(self.sair)

        self.tela_alterar_email.Remover_2.clicked.connect(self.logando) #remover_2 é o voltar
        self.tela_alterar_telefone.Cancelar.clicked.connect(self.logando)
        self.tela_alterar_senha.Cancelar.clicked.connect(self.logando)
        
        self.tela_monitor.EmailBotao.clicked.connect(self.alterar_email)
        self.tela_coordenador.SenhaBotao_2.clicked.connect(self.alterar_email)
        self.tela_tecnico.SenhaBotao_2.clicked.connect(self.alterar_email)
        self.tela_professor.SenhaBotao_2.clicked.connect(self.alterar_email)
        
        self.tela_monitor.TelefoneBotao.clicked.connect(self.alterar_telefone)
        self.tela_coordenador.SenhaBotao_3.clicked.connect(self.alterar_telefone)
        self.tela_tecnico.SenhaBotao_3.clicked.connect(self.alterar_telefone)
        self.tela_professor.SenhaBotao_3.clicked.connect(self.alterar_telefone)
        
        self.tela_monitor.SenhaBotao.clicked.connect(self.alterar_senha)
        self.tela_coordenador.SenhaBotao.clicked.connect(self.alterar_senha)
        self.tela_tecnico.SenhaBotao.clicked.connect(self.alterar_senha)
        self.tela_professor.SenhaBotao.clicked.connect(self.alterar_senha)

        self.tela_monitor.CancelarBotao.clicked.connect(self.cancelar)



        
    def entrar_coord(self):
        self.QtStack.setCurrentIndex(1)
        self.tela_inicio.verifica = 3
    def entrar_monit(self):
        self.QtStack.setCurrentIndex(1)
        self.tela_inicio.verifica = 1
    
    def entrar_prof(self):
        self.QtStack.setCurrentIndex(1)
        self.tela_inicio.verifica = 2

    def entrar_tec(self):
         self.QtStack.setCurrentIndex(1)
         self.tela_inicio.verifica = 4
        
    def voltar(self):
        self.tela_login.verifica = 0
        self.QtStack.setCurrentIndex(0)
        
    def logando(self):
        if( self.tela_inicio.verifica == 3):
            if( "@" in self.tela_login.CampoEmail.text()):
                dados = "l"+","+"c"+","+self.tela_login.CampoEmail.text()+","+self.tela_login.CampoSenha.text()
                
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    self.QtStack.setCurrentIndex(2)
            
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
            else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)
                
        if(self.tela_inicio.verifica == 2):
             if( "@" in self.tela_login.CampoEmail.text()):
                dados = "l"+","+"p"+","+self.tela_login.CampoEmail.text()+","+self.tela_login.CampoSenha.text()
                
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    self.QtStack.setCurrentIndex(3)
            
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
             else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)

                
                
        if(self.tela_inicio.verifica == 1):
             if( "@" in self.tela_login.CampoEmail.text()):
                dados = "l"+","+"m"+","+self.tela_login.CampoEmail.text()+","+self.tela_login.CampoSenha.text()
                print("lixo",dados)
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    self.QtStack.setCurrentIndex(4)
            
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
             else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)
                
        if(self.tela_inicio.verifica == 4):
            if( "@" in self.tela_login.CampoEmail.text()):
                dados = "l"+","+"t"+","+self.tela_login.CampoEmail.text()+","+self.tela_login.CampoSenha.text()
                
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    self.QtStack.setCurrentIndex(5)
            
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
            else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)


            
    def redifinir_senha(self):
        pass

    def cancelar(self):
        self.QtStack.setCurrentIndex(1)

    def alterar_email(self):
        self.QtStack.setCurrentIndex(6)

    def alterar_telefone(self):
        self.QtStack.setCurrentIndex(7)

    def alterar_senha(self):
        self.QtStack.setCurrentIndex(8)
        
    def sair(self):
        sys.exit(app.exec_())
        
            
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

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
from hashlib import md5
from redefinirSenha import Ui_RedefinirSenha
from cliente import cliente
from tela_esq_senha import Ui_Senha
from tecnico import tecnico
from monitor import monitor
from professor import professor
from coordenador import coordenador
from verificaEmail import verificaEmail,verificaTelefone
from valida_dados import verifica_email
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
        self.titulo.setGeometry(QtCore.QRect(180, 40, 301, 31))
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
        self.titulo.setText(_translate("MainWindow", "BEM-VINDO AO RESERVINHA"))
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

        self.stack9 = QtWidgets.QMainWindow()
        
        
            
        self.tela_inicio = Ui_inicio()
        self.tela_login = Ui_Login()
        self.tela_coordenador = Ui_MenuCoordenador()
        self.tela_professor = Ui_MenuProfessor()
        self.tela_monitor = Ui_MenuMonitor()
        self.tela_tecnico = Ui_MenuTecnico()
        self.tela_alterar_email = Ui_AlterarEMAIL()
        self.tela_alterar_telefone = Ui_AlterarTELEFONE()
        self.tela_alterar_senha = Ui_RedefinirSenha()
        self.tela_esq_senha = Ui_Senha()
        
        self.tela_inicio.setupUi(self.stack0)
        self.tela_login.setupUi(self.stack1)
        self.tela_coordenador.setupUi(self.stack2)
        self.tela_professor.setupUi(self.stack3)
        self.tela_monitor.setupUi(self.stack4)
        self.tela_tecnico.setupUi(self.stack5)        
        self.tela_alterar_email.setupUi(self.stack6)
        self.tela_alterar_telefone.setupUi(self.stack7)
        self.tela_alterar_senha.setupUi(self.stack8)
        
        self.tela_esq_senha.setupUi(self.stack9)
        
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)
        self.QtStack.addWidget(self.stack8)
        self.QtStack.addWidget(self.stack9)
        



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
        self.tela_alterar_email.Remover.clicked.connect(self.alterar_email_tela)
        
        self.tela_alterar_telefone.Cancelar.clicked.connect(self.logando)
        self.tela_alterar_senha.Cancelar.clicked.connect(self.logando)
        self.tela_alterar_senha.Redefinir.clicked.connect(self.alterar_senha_tela)
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
        self.tela_login.EsqueceuSenha.clicked.connect(self.redefinir_senha)

        self.tela_esq_senha.codigo.clicked.connect(self.cancelar)
        
        self.tela_alterar_telefone.Alterar.clicked.connect(self.alterar_telefone_tela)
        
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
                dados = "l"+","+"c"+","+self.tela_login.CampoEmail.text()+","+md5(self.tela_login.CampoSenha.text().encode('utf-8')).hexdigest()
                
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    dados = c1.client_socket.recv(2048).decode()
                    #print("Dados",dados)
                    lista = dados.split(",")
                    print("A lista",lista)
                    
                    self.coord = coordenador(None,None,None,None,None,None)
                    self.coord.setTelefone(lista[5])
                    self.coord.setCpf(lista[2])
                    self.coord.setSiape(int(lista[1]))
                    self.coord.setNome(lista[0])
                    self.coord.setCurso(lista[6])
                    self.coord.setEmail(lista[4])
                    self.coord.setSenha(lista[3])
                    print("Nome",self.coord.getNome())
                    print("Siape",self.coord.getSIAPE())
                    print("Cpf",self.coord.getCpf())
                    print("Senha",self.coord.getSenha())
                    print("Email:",self.coord.getEmail())
                    print("Telefone",self.coord.getTelefone())
                    print("Disciplina",self.coord.getCurso())
                    
                    self.tela_coordenador.loga_coordenador(self.coord)
                    self.tela_alterar_email.getPessoa(self.coord)
                    self.tela_alterar_telefone.getPessoa(self.coord)
                    self.tela_alterar_senha.getPessoa(self.coord)
                    
                                        
                    self.QtStack.setCurrentIndex(2)
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
            else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)
                
        if(self.tela_inicio.verifica == 2):
             if( "@" in self.tela_login.CampoEmail.text()):
                dados = "l"+","+"p"+","+self.tela_login.CampoEmail.text()+","+md5(self.tela_login.CampoSenha.text().encode('utf-8')).hexdigest()
                
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    dados = c1.client_socket.recv(2048).decode()
                    lista = dados.split(",")
                    print("A lista",lista)
                    self.prof = professor(None,None,None,None,None,None,None)
                    self.prof.setTelefone(lista[5])
                    self.prof.setCpf(lista[2])
                    self.prof.setSiape(int(lista[1]))
                    self.prof.setNome(lista[0])
                    self.prof.setDisciplina(lista[6])
                    self.prof.setEmail(lista[4])
                    self.prof.setSenha(lista[3])
                    print("Nome",self.prof.getNome())
                    print("Siape",self.prof.getSIAPE())
                    print("Cpf",self.prof.getCpf())
                    print("Senha",self.prof.getSenha())
                    print("Email:",self.prof.getEmail())
                    print("Telefone",self.prof.getTelefone())
                    print("Disciplina",self.prof.getDisciplina())

                    self.tela_professor.loga_professor(self.prof)
                    
                    self.tela_alterar_email.getPessoa(self.prof)
                    self.tela_alterar_telefone.getPessoa(self.prof)
                    self.tela_alterar_senha.getPessoa(self.prof)
                    
                    
                    
                    self.QtStack.setCurrentIndex(3)
                    
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
             else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)

                
                
        if(self.tela_inicio.verifica == 1):
             if( "@" in self.tela_login.CampoEmail.text()):
                dados = "l"+","+"m"+","+self.tela_login.CampoEmail.text()+","+md5(self.tela_login.CampoSenha.text().encode('utf-8')).hexdigest()
                print("lixo",dados)
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    dados = c1.client_socket.recv(2048).decode()
                    lista = dados.split(",")
                    print("A lista",lista)
                    self.monit = monitor(None,None,None,None,None,None,None,None)
                    self.monit.setTelefone(lista[5])
                    self.monit.setCpf(lista[2])
                    self.monit.setMatricula(int(lista[1]))
                    self.monit.setNome(lista[0])
                    self.monit.setDisciplina(lista[6])
                    self.monit.setEmail(lista[4])
                    self.monit.setSenha(lista[3])
                    print("Nome",self.monit.getNome())
                    print("Matricula",self.monit.getMatricula())
                    print("Cpf",self.monit.getCpf())
                    print("Senha",self.monit.getSenha())
                    print("Email:",self.monit.getEmail())
                    print("Telefone",self.monit.getTelefone())
                    print("Disciplina",self.monit.getDisciplina())

                    self.tela_alterar_email.getPessoa(self.monit)
                    self.tela_alterar_telefone.getPessoa(self.monit)
                    self.tela_alterar_senha.getPessoa(self.monit)
                    
                    
                    
                    self.tela_monitor.loga_monitor(self.monit)
                    self.QtStack.setCurrentIndex(4)
            
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
             else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)
                
        if(self.tela_inicio.verifica == 4):
            if( "@" in self.tela_login.CampoEmail.text()):
                dados = "l"+","+"t"+","+self.tela_login.CampoEmail.text()+","+md5(self.tela_login.CampoSenha.text().encode('utf-8')).hexdigest()
                
                c1 = cliente(dados)
                if(c1.client_socket.recv(1024).decode()=="plog"):
                    dados = c1.client_socket.recv(2048).decode()
                    lista = dados.split(",")
                    print("A lista",lista)
                    self.tec = tecnico(None,None,None,None,None)
                    self.tec.setTelefone(lista[3])
                    self.tec.setCpf(lista[1])
                    self.tec.setNome(lista[0])
                    self.tec.setEmail(lista[2])
                    self.tec.setSenha(lista[4])
                    print("Nome",self.tec.getNome())
                    print("Cpf",self.tec.getCpf())
                    print("Senha",self.tec.getSenha())
                    print("Email:",self.tec.getEmail())
                    print("Telefone",self.tec.getTelefone())
                    self.tela_tecnico.loga_tecnico(self.tec)

                    self.tela_alterar_email.getPessoa(self.tec)
                    self.tela_alterar_telefone.getPessoa(self.tec)
                    self.tela_alterar_senha.getPessoa(self.tec)
                    
                    self.QtStack.setCurrentIndex(5)
            
                else:
                    QtWidgets.QMessageBox.about(None, "AVISO","SENHA OU EMAIL INVALIDOS",)
            else:
                QtWidgets.QMessageBox.about(None, "AVISO","EMAIL INVALIDO",)


            
    def redefinir_senha(self):
        self.QtStack.setCurrentIndex(9)
        
        
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

    def alterar_telefone_tela(self):
        telefone = self.tela_alterar_telefone.CampoTelefone.text()
        if(verificaTelefone(telefone)):
            string = ''
            if(type(self.tela_alterar_telefone.pessoa) is coordenador):
                    string = "altera_telefone"+","+"c"+","+telefone+","+self.tela_alterar_telefone.pessoa.getTelefone()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.coord.setTelefone(telefone)
                        
                        QtWidgets.QMessageBox.information(None, "AVISO","Telefone redefinido com sucesso!",)
                        self.tela_alterar_telefone.CampoTelefone.clear()
                        
                        self.tela_alterar_telefone.getPessoa(self.coord)
                        
                        
                        print("Teste",self.tela_alterar_telefone.pessoa.getTelefone())
                        
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este número ja está cadastrado!",)
                        
            if(type(self.tela_alterar_telefone.pessoa) is monitor):
                    string = "altera_telefone"+","+"m"+","+telefone+","+self.tela_alterar_telefone.pessoa.getTelefone()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.monit.setTelefone(telefone)
                        
                        QtWidgets.QMessageBox.information(None, "AVISO","Telefone redefinido com sucesso!",)
                        self.tela_alterar_telefone.CampoTelefone.clear()
                        
                        self.tela_alterar_telefone.getPessoa(self.monit)
                        
                        
                        print("Teste",self.tela_alterar_telefone.pessoa.getTelefone())
                        
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este número ja está cadastrado!",)
                        
            if(type(self.tela_alterar_telefone.pessoa) is professor):
                    string = "altera_telefone"+","+"p"+","+telefone+","+self.tela_alterar_telefone.pessoa.getTelefone()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.prof.setTelefone(telefone)
                        
                        QtWidgets.QMessageBox.information(None, "AVISO","Telefone redefinido com sucesso!",)
                        self.tela_alterar_telefone.CampoTelefone.clear()
                        
                        self.tela_alterar_telefone.getPessoa(self.prof)
                        
                        
                        print("Teste",self.tela_alterar_telefone.pessoa.getTelefone())
                        
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este número ja está cadastrado!",)


            if(type(self.tela_alterar_telefone.pessoa) is tecnico):
                    string = "altera_telefone"+","+"t"+","+telefone+","+self.tela_alterar_telefone.pessoa.getTelefone()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.tec.setTelefone(telefone)
                        
                        QtWidgets.QMessageBox.information(None, "AVISO","Telefone redefinido com sucesso!",)
                        self.tela_alterar_telefone.CampoTelefone.clear()
                        
                        self.tela_alterar_telefone.getPessoa(self.tec)
                        
                        
                        print("Teste",self.tela_alterar_telefone.pessoa.getTelefone())
                        
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este número ja está cadastrado!",)



                        

        else:
            QtWidgets.QMessageBox.warning(None, "AVISO","TELEFONE INVÁLIDO DIGITADO!",)
            
    def alterar_email_tela(self):
        email = self.tela_alterar_email.lineEdit.text()
        email2 = self.tela_alterar_email.lineEdit_2.text()
        if(verificaEmail(email)):
            if(email==email2):
                string = ''
            
                if(type(self.tela_alterar_email.pessoa) is coordenador):
                    string = "altera_email"+","+"c"+","+email+","+self.tela_alterar_email.pessoa.getEmail()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.coord.setEmail(email)
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                        QtWidgets.QMessageBox.information(None, "AVISO","Email redefinido com sucesso!",)
                        self.tela_alterar_email.lineEdit.clear()
                        self.tela_alterar_email.lineEdit_2.clear()
                        self.tela_alterar_email.getPessoa(self.coord)
                        
                        
                        print("Teste",self.tela_alterar_email.pessoa.getEmail())
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este email ja está cadastrado!",)
                        
                if(type(self.tela_alterar_email.pessoa) is monitor):
                    string = "altera_email"+","+"m"+","+email+","+self.tela_alterar_email.pessoa.getEmail()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.monit.setEmail(email)
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                        QtWidgets.QMessageBox.information(None, "AVISO","Email redefinido com sucesso!",)
                        self.tela_alterar_email.lineEdit.clear()
                        self.tela_alterar_email.lineEdit_2.clear()
                        self.tela_alterar_email.getPessoa(self.monit)
                        
                        
                        print("Teste",self.tela_alterar_email.pessoa.getEmail())
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este email ja está cadastrado!",)
                if(type(self.tela_alterar_email.pessoa) is professor):
                    string = "altera_email"+","+"p"+","+email+","+self.tela_alterar_email.pessoa.getEmail()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.prof.setEmail(email)
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                        QtWidgets.QMessageBox.information(None, "AVISO","Email redefinido com sucesso!",)
                        self.tela_alterar_email.lineEdit.clear()
                        self.tela_alterar_email.lineEdit_2.clear()
                        self.tela_alterar_email.getPessoa(self.prof)
                        
                        
                        print("Teste",self.tela_alterar_email.pessoa.getEmail())
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este email ja está cadastrado!",)
                if(type(self.tela_alterar_email.pessoa) is tecnico):
                    string = "altera_email"+","+"t"+","+email+","+self.tela_alterar_email.pessoa.getEmail()
                    c1 = cliente(string)
                    if(c1.client_socket.recv(1024).decode()=="mudou"):
                        self.tec.setEmail(email)
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                        QtWidgets.QMessageBox.information(None, "AVISO","Email redefinido com sucesso!",)
                        self.tela_alterar_email.lineEdit.clear()
                        self.tela_alterar_email.lineEdit_2.clear()
                        self.tela_alterar_email.getPessoa(self.tec)
                        
                        
                        print("Teste",self.tela_alterar_email.pessoa.getEmail())
                        self.tela_login.CampoEmail.setText(self.tela_alterar_email.pessoa.getEmail())
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","Este email ja está cadastrado!",)

                
            else:
               QtWidgets.QMessageBox.warning(None, "AVISO","CONFIRME O NOVO EMAIL EM AMBOS OS CAMPOS",)  
        else:
           QtWidgets.QMessageBox.warning(None, "AVISO","EMAIL INVÁLIDO DIGITADO!",) 

    def alterar_senha_tela(self):
        senha_antiga = self.tela_alterar_senha.CampoSenhaAntiga.text()
        senha_nova = self.tela_alterar_senha.CampoNovaSenha.text()
        conf = self.tela_alterar_senha.CampoConfirmar.text()
        mdcomp = md5(senha_antiga.encode('utf-8')).hexdigest()
        print("A senha antiga",senha_antiga)
        if(len(senha_antiga)==0 or len(senha_nova) == 0 or len(conf)==0):
            QtWidgets.QMessageBox.warning(None, "AVISO","PREENCHA TODOS OS CAMPOS!",)
            
        else:
            if(conf==senha_nova):
                if(type(self.tela_alterar_senha.pessoa) is coordenador):
                    print("1",mdcomp)
                    print("2",self.tela_alterar_senha.pessoa.getSenha())
                    if(mdcomp == self.tela_alterar_senha.pessoa.getSenha()):
                        string = "altera_senha"+","+"c"+","+senha_nova+","+senha_antiga
                        c1 = cliente(string)
                        if(c1.client_socket.recv(1024).decode()=="mudou"):
                            self.coord.setSenha(md5(senha_nova.encode('utf-8')).hexdigest())
                            self.tela_login.CampoSenha.setText(senha_nova)
                            QtWidgets.QMessageBox.information(None, "AVISO","Senha redefinida com sucesso!",)
                            self.tela_alterar_senha.CampoSenhaAntiga.clear()
                            self.tela_alterar_senha.CampoNovaSenha.clear()
                            self.tela_alterar_senha.CampoConfirmar.clear()
                            self.tela_alterar_senha.getPessoa(self.coord)
                            
                            
                        else:
                            QtWidgets.QMessageBox.warning(None, "AVISO","Esta senha já está cadastrada",)
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","SENHA INCORRETA",)
                if(type(self.tela_alterar_senha.pessoa) is professor):
                    
                    if(mdcomp == self.tela_alterar_senha.pessoa.getSenha()):
                        string = "altera_senha"+","+"p"+","+senha_nova+","+senha_antiga
                        c1 = cliente(string)
                        if(c1.client_socket.recv(1024).decode()=="mudou"):
                            self.prof.setSenha(md5(senha_nova.encode('utf-8')).hexdigest())
                            self.tela_login.CampoSenha.setText(senha_nova)
                            QtWidgets.QMessageBox.information(None, "AVISO","Senha redefinida com sucesso!",)
                            self.tela_alterar_senha.CampoSenhaAntiga.clear()
                            self.tela_alterar_senha.CampoNovaSenha.clear()
                            self.tela_alterar_senha.CampoConfirmar.clear()
                            self.tela_alterar_senha.getPessoa(self.prof)
                            
                            
                        else:
                            QtWidgets.QMessageBox.warning(None, "AVISO","Esta senha já está cadastrada",)
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","SENHA INCORRETA",)

                if(type(self.tela_alterar_senha.pessoa) is monitor):
                    
                    if(mdcomp == self.tela_alterar_senha.pessoa.getSenha()):
                        string = "altera_senha"+","+"m"+","+senha_nova+","+senha_antiga
                        c1 = cliente(string)
                        if(c1.client_socket.recv(1024).decode()=="mudou"):
                            self.monit.setSenha(md5(senha_nova.encode('utf-8')).hexdigest())
                            self.tela_login.CampoSenha.setText(senha_nova)
                            QtWidgets.QMessageBox.information(None, "AVISO","Senha redefinida com sucesso!",)
                            self.tela_alterar_senha.CampoSenhaAntiga.clear()
                            self.tela_alterar_senha.CampoNovaSenha.clear()
                            self.tela_alterar_senha.CampoConfirmar.clear()
                            self.tela_alterar_senha.getPessoa(self.monit)
                            
                            
                        else:
                            QtWidgets.QMessageBox.warning(None, "AVISO","Esta senha já está cadastrada",)
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","SENHA INCORRETA",)

                if(type(self.tela_alterar_senha.pessoa) is tecnico):
                    
                    if(mdcomp == self.tela_alterar_senha.pessoa.getSenha()):
                        string = "altera_senha"+","+"t"+","+senha_nova+","+senha_antiga
                        c1 = cliente(string)
                        if(c1.client_socket.recv(1024).decode()=="mudou"):
                            self.tec.setSenha(md5(senha_nova.encode('utf-8')).hexdigest())
                            self.tela_login.CampoSenha.setText(senha_nova)
                            QtWidgets.QMessageBox.information(None, "AVISO","Senha redefinida com sucesso!",)
                            self.tela_alterar_senha.CampoSenhaAntiga.clear()
                            self.tela_alterar_senha.CampoNovaSenha.clear()
                            self.tela_alterar_senha.CampoConfirmar.clear()
                            self.tela_alterar_senha.getPessoa(self.tec)
                            
                            
                        else:
                            QtWidgets.QMessageBox.warning(None, "AVISO","Esta senha já está cadastrada",)
                    else:
                        QtWidgets.QMessageBox.warning(None, "AVISO","SENHA INCORRETA",)

                
                    
            else:
               QtWidgets.QMessageBox.warning(None, "AVISO","CONFIRME A NOVA SENHA DE MANEIRA CORRETA!",) 
        
             
        
            
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())

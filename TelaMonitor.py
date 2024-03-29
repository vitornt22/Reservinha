# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Monitor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from cliente import cliente
from verificaEmail import verificaEmail,verificaCpf,verificaTelefone,verificaMat
from geradordepdf import GeraPDF
from enviaemail import envia_email
class Ui_MenuMonitor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(732, 482)
        self.r_message = False
        MainWindow.setAutoFillBackground(False)
        MainWindow.setAnimated(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TabelaGeral = QtWidgets.QTabWidget(self.centralwidget)
        self.TabelaGeral.setGeometry(QtCore.QRect(0, 0, 741, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TabelaGeral.setFont(font)
        self.TabelaGeral.setStyleSheet("QWidget{\n"
"    color: rgb(3, 0, 117)\n"
"}")
        self.TabelaGeral.setObjectName("TabelaGeral")
        self.ReservaSala = QtWidgets.QWidget()
        self.ReservaSala.setObjectName("ReservaSala")
        self.Fundo = QtWidgets.QLabel(self.ReservaSala)
        self.Fundo.setGeometry(QtCore.QRect(-10, -60, 741, 531))
        self.Fundo.setText("")
        self.Fundo.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.Fundo.setObjectName("Fundo")
        self.layoutWidget = QtWidgets.QWidget(self.ReservaSala)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 144))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.agrupamento9 = QtWidgets.QHBoxLayout()
        self.agrupamento9.setObjectName("agrupamento9")
        self.Bloco = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Bloco.setFont(font)
        self.Bloco.setObjectName("Bloco")
        self.agrupamento9.addWidget(self.Bloco)
        self.CampoBloco = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoBloco.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoBloco.setObjectName("CampoBloco")
        self.agrupamento9.addWidget(self.CampoBloco)
        self.verticalLayout.addLayout(self.agrupamento9)
        self.agrupamento11 = QtWidgets.QHBoxLayout()
        self.agrupamento11.setObjectName("agrupamento11")
        self.Sala = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sala.setFont(font)
        self.Sala.setObjectName("Sala")
        self.agrupamento11.addWidget(self.Sala)
        self.CampoSala = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoSala.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoSala.setObjectName("CampoSala")
        self.agrupamento11.addWidget(self.CampoSala)
        self.verticalLayout.addLayout(self.agrupamento11)
        self.agrupamento10 = QtWidgets.QHBoxLayout()
        self.agrupamento10.setObjectName("agrupamento10")
        self.Dia = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dia.setFont(font)
        self.Dia.setObjectName("Dia")
        self.agrupamento10.addWidget(self.Dia)
        self.CampoDIa = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoDIa.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoDIa.setObjectName("CampoDIa")
        self.agrupamento10.addWidget(self.CampoDIa)
        self.verticalLayout.addLayout(self.agrupamento10)
        self.agrupamento10_2 = QtWidgets.QHBoxLayout()
        self.agrupamento10_2.setObjectName("agrupamento10_2")
        self.Horario = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Horario.setFont(font)
        self.Horario.setObjectName("Horario")
        self.agrupamento10_2.addWidget(self.Horario)
        self.CampoHorario = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoHorario.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoHorario.setObjectName("CampoHorario")
        self.agrupamento10_2.addWidget(self.CampoHorario)
        self.verticalLayout.addLayout(self.agrupamento10_2)
        self.tabela = QtWidgets.QTableWidget(self.ReservaSala)
        self.tabela.setGeometry(QtCore.QRect(10, 170, 691, 241))
        self.tabela.setObjectName("tabela")
        self.tabela.setColumnCount(6)
        self.tabela.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabela.setHorizontalHeaderItem(5, item)
        self.Reservar = QtWidgets.QPushButton(self.ReservaSala)
        self.Reservar.setGeometry(QtCore.QRect(460, 80, 151, 41))
        self.Reservar.setObjectName("Reservar")
        self.Listar = QtWidgets.QPushButton(self.ReservaSala)
        self.Listar.setGeometry(QtCore.QRect(460, 10, 151, 41))
        self.Listar.setObjectName("Listar")
        self.TabelaGeral.addTab(self.ReservaSala, "")
        self.VerReservas = QtWidgets.QWidget()
        self.VerReservas.setObjectName("VerReservas")
        self.fundo_3 = QtWidgets.QLabel(self.VerReservas)
        self.fundo_3.setGeometry(QtCore.QRect(0, -50, 791, 531))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fundo_3.setFont(font)
        self.fundo_3.setText("")
        self.fundo_3.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_3.setScaledContents(True)
        self.fundo_3.setObjectName("fundo_3")
        self.Mostrar = QtWidgets.QPushButton(self.VerReservas)
        self.Mostrar.setGeometry(QtCore.QRect(240, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mostrar.setFont(font)
        self.Mostrar.setObjectName("Mostrar")
        self.gerarPDF = QtWidgets.QPushButton(self.VerReservas)
        self.gerarPDF.setGeometry(QtCore.QRect(380, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gerarPDF.setFont(font)
        self.gerarPDF.setObjectName("gerarPDF")
        self.listWidget = QtWidgets.QListWidget(self.VerReservas)
        self.listWidget.setGeometry(QtCore.QRect(90, 31, 531, 271))
        self.listWidget.setObjectName("listWidget")
        self.TabelaGeral.addTab(self.VerReservas, "")
        self.CancelarReservas = QtWidgets.QWidget()
        self.CancelarReservas.setObjectName("CancelarReservas")
        self.fundo_4 = QtWidgets.QLabel(self.CancelarReservas)
        self.fundo_4.setGeometry(QtCore.QRect(-130, 20, 931, 401))
        self.fundo_4.setText("")
        self.fundo_4.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_4.setObjectName("fundo_4")
        self.layoutWidget_8 = QtWidgets.QWidget(self.CancelarReservas)
        self.layoutWidget_8.setGeometry(QtCore.QRect(150, 80, 321, 131))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.Agrupamento13_2 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.Agrupamento13_2.setContentsMargins(0, 0, 0, 0)
        self.Agrupamento13_2.setObjectName("Agrupamento13_2")
        self.subagrupamento1_2 = QtWidgets.QHBoxLayout()
        self.subagrupamento1_2.setObjectName("subagrupamento1_2")
        self.Bloco_4 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bloco_4.setFont(font)
        self.Bloco_4.setObjectName("Bloco_4")
        self.subagrupamento1_2.addWidget(self.Bloco_4)
        self.CampoBloco_4 = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.CampoBloco_4.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoBloco_4.setObjectName("CampoBloco_4")
        self.subagrupamento1_2.addWidget(self.CampoBloco_4)
        self.Agrupamento13_2.addLayout(self.subagrupamento1_2)
        self.subagrupamento2_2 = QtWidgets.QHBoxLayout()
        self.subagrupamento2_2.setObjectName("subagrupamento2_2")
        self.Sala_3 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sala_3.setFont(font)
        self.Sala_3.setObjectName("Sala_3")
        self.subagrupamento2_2.addWidget(self.Sala_3)
        self.CampoSala_3 = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.CampoSala_3.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoSala_3.setObjectName("CampoSala_3")
        self.subagrupamento2_2.addWidget(self.CampoSala_3)
        self.Agrupamento13_2.addLayout(self.subagrupamento2_2)
        self.subagrupamento3_2 = QtWidgets.QHBoxLayout()
        self.subagrupamento3_2.setObjectName("subagrupamento3_2")
        self.Dia_4 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Dia_4.setFont(font)
        self.Dia_4.setObjectName("Dia_4")
        self.subagrupamento3_2.addWidget(self.Dia_4)
        self.CampoDia_2 = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.CampoDia_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoDia_2.setObjectName("CampoDia_2")
        self.subagrupamento3_2.addWidget(self.CampoDia_2)
        self.Agrupamento13_2.addLayout(self.subagrupamento3_2)
        self.Remover = QtWidgets.QPushButton(self.CancelarReservas)
        self.Remover.setGeometry(QtCore.QRect(260, 260, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remover.setFont(font)
        self.Remover.setObjectName("Remover")
        self.layoutWidget_9 = QtWidgets.QWidget(self.CancelarReservas)
        self.layoutWidget_9.setGeometry(QtCore.QRect(150, 210, 321, 31))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.subagrupamento3_3 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.subagrupamento3_3.setContentsMargins(0, 0, 0, 0)
        self.subagrupamento3_3.setObjectName("subagrupamento3_3")
        self.horario = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.horario.setFont(font)
        self.horario.setObjectName("horario")
        self.subagrupamento3_3.addWidget(self.horario)
        self.CampoHorario_2 = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.CampoHorario_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoHorario_2.setObjectName("CampoHorario_2")
        self.subagrupamento3_3.addWidget(self.CampoHorario_2)
        self.TabelaGeral.addTab(self.CancelarReservas, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.fundo_5 = QtWidgets.QLabel(self.tab)
        self.fundo_5.setGeometry(QtCore.QRect(0, 0, 931, 401))
        self.fundo_5.setText("")
        self.fundo_5.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_5.setObjectName("fundo_5")
        self.EmailBotao = QtWidgets.QPushButton(self.tab)
        self.EmailBotao.setGeometry(QtCore.QRect(240, 140, 171, 41))
        self.EmailBotao.setObjectName("EmailBotao")
        self.SenhaBotao = QtWidgets.QPushButton(self.tab)
        self.SenhaBotao.setGeometry(QtCore.QRect(240, 90, 171, 41))
        self.SenhaBotao.setObjectName("SenhaBotao")
        self.TelefoneBotao = QtWidgets.QPushButton(self.tab)
        self.TelefoneBotao.setGeometry(QtCore.QRect(240, 190, 171, 41))
        self.TelefoneBotao.setObjectName("TelefoneBotao")
        self.CancelarBotao = QtWidgets.QPushButton(self.tab)
        self.CancelarBotao.setGeometry(QtCore.QRect(240, 240, 171, 41))
        self.CancelarBotao.setObjectName("CancelarBotao")
        self.TabelaGeral.addTab(self.tab, "")
        self.Informacoes = QtWidgets.QWidget()
        self.Informacoes.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Informacoes.setObjectName("Informacoes")
        self.fundo_6 = QtWidgets.QLabel(self.Informacoes)
        self.fundo_6.setGeometry(QtCore.QRect(-10, 0, 931, 451))
        self.fundo_6.setText("")
        self.fundo_6.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_6.setObjectName("fundo_6")
        self.widget = QtWidgets.QWidget(self.Informacoes)
        self.widget.setGeometry(QtCore.QRect(60, 240, 471, 36))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mat = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.mat.setFont(font)
        self.mat.setObjectName("mat")
        self.horizontalLayout.addWidget(self.mat)
        self.LabelSiape = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabelSiape.setFont(font)
        self.LabelSiape.setText("")
        self.LabelSiape.setObjectName("LabelSiape")
        self.horizontalLayout.addWidget(self.LabelSiape)
        self.widget1 = QtWidgets.QWidget(self.Informacoes)
        self.widget1.setGeometry(QtCore.QRect(60, 180, 471, 36))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.email = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.horizontalLayout_2.addWidget(self.email)
        self.LabeEmail = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabeEmail.setFont(font)
        self.LabeEmail.setText("")
        self.LabeEmail.setObjectName("LabeEmail")
        self.horizontalLayout_2.addWidget(self.LabeEmail)
        self.widget2 = QtWidgets.QWidget(self.Informacoes)
        self.widget2.setGeometry(QtCore.QRect(60, 130, 471, 36))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.telefone = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.telefone.setFont(font)
        self.telefone.setObjectName("telefone")
        self.horizontalLayout_3.addWidget(self.telefone)
        self.LabelTelefone = QtWidgets.QLabel(self.widget2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabelTelefone.setFont(font)
        self.LabelTelefone.setText("")
        self.LabelTelefone.setObjectName("LabelTelefone")
        self.horizontalLayout_3.addWidget(self.LabelTelefone)
        self.widget3 = QtWidgets.QWidget(self.Informacoes)
        self.widget3.setGeometry(QtCore.QRect(60, 80, 471, 36))
        self.widget3.setObjectName("widget3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.nome = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nome.setFont(font)
        self.nome.setObjectName("nome")
        self.horizontalLayout_4.addWidget(self.nome)
        self.LabelNome = QtWidgets.QLabel(self.widget3)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabelNome.setFont(font)
        self.LabelNome.setText("")
        self.LabelNome.setObjectName("LabelNome")
        self.horizontalLayout_4.addWidget(self.LabelNome)
        self.TabelaGeral.addTab(self.Informacoes, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabelaGeral.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MENU MONITOR"))
        self.Bloco.setText(_translate("MainWindow", "BLOCO"))
        self.Sala.setText(_translate("MainWindow", "SALA    "))
        self.Dia.setText(_translate("MainWindow", "DIA       "))
        self.Horario.setText(_translate("MainWindow", "Horário "))
        item = self.tabela.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "8:00 - 10:00"))
        item = self.tabela.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "10:00 - 12:00"))
        item = self.tabela.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "12:00 - 14:00"))
        item = self.tabela.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "14:00 - 16:00"))
        item = self.tabela.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "16:00 - 18:00"))
        item = self.tabela.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "18:00- 20:00"))
        item = self.tabela.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "20:00- 22:00"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Segunda"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Terça"))
        item = self.tabela.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Quarta"))
        item = self.tabela.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Quinta"))
        item = self.tabela.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sexta"))
        item = self.tabela.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Sabado"))
        self.Reservar.setText(_translate("MainWindow", "Reservar"))
        self.Listar.setText(_translate("MainWindow", "Listar Horários"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.ReservaSala), _translate("MainWindow", "Reservar Sala"))
        self.Mostrar.setText(_translate("MainWindow", "MOSTRAR"))
        self.gerarPDF.setText(_translate("MainWindow", "GERAR PDF"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.VerReservas), _translate("MainWindow", "Ver reservas"))
        self.Bloco_4.setText(_translate("MainWindow", "BLOCO"))
        self.Sala_3.setText(_translate("MainWindow", "SALA    "))
        self.Dia_4.setText(_translate("MainWindow", "DIA      "))
        self.Remover.setText(_translate("MainWindow", "REMOVER"))
        self.horario.setText(_translate("MainWindow", "HORARIO"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.CancelarReservas), _translate("MainWindow", "Cancelar reserva"))
        self.EmailBotao.setText(_translate("MainWindow", "EMAIL"))
        self.SenhaBotao.setText(_translate("MainWindow", "SENHA"))
        self.TelefoneBotao.setText(_translate("MainWindow", "TELEFONE"))
        self.CancelarBotao.setText(_translate("MainWindow", "CANCELAR"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.tab), _translate("MainWindow", "Alterar Dados"))
        self.mat.setText(_translate("MainWindow", "MATRICULA"))
        self.email.setText(_translate("MainWindow", "EMAIL"))
        self.telefone.setText(_translate("MainWindow", "TELEFONE:"))
        self.nome.setText(_translate("MainWindow", "NOME"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.Informacoes), _translate("MainWindow", "Informações"))
        self.funcionalidade()
        
    def funcionalidade(self):
        self.Listar.clicked.connect(self.listar_salas)
        self.Reservar.clicked.connect(self.reservar)
        self.Mostrar.clicked.connect(self.mostrar_reservas)
        self.gerarPDF.clicked.connect(self.gera_pdf)
        self.Remover.clicked.connect(self.cancelar_reserva)
    def mostrar(self):
        self.LabelNome.setText(self.monitor.getNome())
        self.LabelTelefone.setText(self.monitor.getTelefone())
        self.LabeEmail.setText(self.monitor.getEmail())
        self.LabelSiape.setText(str(self.monitor.getMatricula()))
        """print("Nome",self.monitor.getNome())
        print("Siape",self.monitor.getMatricula())
        print("Cpf",self.monitor.getCpf())
        print("Senha",self.monitor.getSenha())
        print("Email:",self.monitor.getEmail())
        print("Telefone",self.monitor.getTelefone())
        print("Matricula",self.monitor.getDisciplina())"""
        
    def loga_monitor(self,monitor1):
        self.monitor = monitor1
        if(not self.r_message):
            QtWidgets.QMessageBox.information(None, "AVISO","Bem vindo monitor: "+self.monitor.getNome(),)
            self.r_message = True
        self.mostrar()
    def listar_salas(self):
        #self.CampoDIa.setText("vitor burro") campo do dia
        #self.CampoBloco.setText("lixo") bloco
        #self.CampoSala.setText("819") sala
        #self.CampoHorario.setText("2") horario
        string = ''
        erros = ''
        if((len(self.CampoBloco.text())==0) or (len(self.CampoSala.text())==0)):
            QtWidgets.QMessageBox.warning(None, "AVISO","PREENCHA CAMPOS BLOCO E SALA PARA PODER VER A TABELA DE RESERVAS",)
        else:
            
            if(len(erros)>0):
               QtWidgets.QMessageBox.warning(None, "AVISO","Dados inválidos nos seguintes campos: "+erros,)
            else:
                string = "Listar"+","+self.CampoBloco.text()+","+self.CampoSala.text()
                c1 = cliente(string)
                str2 = c1.client_socket.recv(1024).decode()
                if(str2=="vazio"):
                    QtWidgets.QMessageBox.warning(None, "AVISO","Bloco ou Sala não cadastrados",)
                else:
                    lista = str2.split(",")
                    lista.pop(len(lista)-1)
                
                    c = 0
    
                    for j in range(6):
                        for i in range(7):
                            self.tabela.setItem(i,j, QtWidgets.QTableWidgetItem(lista[c]))
                            c+=1


    def reservar(self):
        string = ''
        if((len(self.CampoBloco.text())==0) or (len(self.CampoSala.text())==0) or (len(self.CampoHorario.text())==0) or len(self.CampoDIa.text())==0):
            QtWidgets.QMessageBox.warning(None, "AVISO","PREENCHA TODOS OS CAMPOS PARA RESERVAR UMA SALA",)
        else:
            string = "reservar"+","+self.monitor.getCpf()+","+self.CampoBloco.text()+","+self.CampoSala.text()+","+self.CampoDIa.text()+","+self.CampoHorario.text()
            c1 = cliente(string)
            string2 = c1.client_socket.recv(1024).decode()
            print("String2",string2)
            if(string2=="certo"):
                QtWidgets.QMessageBox.information(None, "AVISO","Reserva efetuada com sucesso",)
            else:
               QtWidgets.QMessageBox.warning(None, "AVISO","Não foi possível realizar a reserva!",) 

    def mostrar_reservas(self):
        string = 'mostrar'+","+self.monitor.getCpf()
        c1 = cliente(string)
        string2 = c1.client_socket.recv(1024).decode()
        lista = []
        self.listWidget.clear()
        if("recebido" in string2):
            string2 = c1.client_socket.recv(1024).decode()
            lista = string2.split(",")
            
            self.listWidget.addItem("                                                    SALA                       HORARIO                    DIA")
            print("The lista",lista)
            lista.pop(len(lista)-1)
            cont = 0
            while(cont<len(lista)):
                
                self.listWidget.addItem("                                                     "+lista[cont]+"                            "+lista[cont+1]+"                "+lista[cont+2])                                               
                cont+=3
        else:
            QtWidgets.QMessageBox.information(None, "AVISO","Não há reservas realizadas no momento",) 

    def gera_pdf(self):
        string = 'solicita'+","+self.monitor.getCpf()+","+self.monitor.getEmail()
        c1 = cliente(string)
        
        string2 = c1.client_socket.recv(1024).decode()
        
        
        lista = string2.split(",")
        print(lista)
        if(lista[0]!="invalido"):
            g = GeraPDF(self.monitor,lista[0],lista[1])
            g.cria()
            envia = envia_email(self.monitor)
            envia.send_an_email()
            QtWidgets.QMessageBox.information(None, "AVISO","Email enviado com sucesso",)

    def cancelar_reserva(self):
        bloco = self.CampoBloco_4.text()
        sala = self.CampoSala_3.text()
        dia = self.CampoDia_2.text()
        horario = self.CampoHorario_2.text()
        string = ''
        if(len(dia)== 0 or len(sala) == 0 or len(bloco)==0 or len(horario)==0):
            QtWidgets.QMessageBox.information(None, "AVISO","PREENCHA TODOS OS CAMPOS!",)
        else:
            string = "cancelar_reserva"+","+self.monitor.getCpf()+","+bloco+","+sala+","+dia+","+horario
            c1 = cliente(string)
            string2 = c1.client_socket.recv(1024).decode()
            if(string2=="cancelar"):
                QtWidgets.QMessageBox.information(None, "AVISO","Reserva cancelada com sucesso",)
                self.CampoBloco_4.clear()
                self.CampoSala_3.clear()
                self.CampoDia_2.clear()
                self.CampoHorario_2.clear()

            else:
                QtWidgets.QMessageBox.warning(None, "AVISO","Não há reservas para serem canceladas",)
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuMonitor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


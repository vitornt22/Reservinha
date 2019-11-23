# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaProfessor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from verificaEmail import verificaEmail,verificaCpf,verificaTelefone,verificaMat
from cliente import cliente
class Ui_MenuProfessor(object):
    def setupUi(self, MenuProfessor):
        self.professor = None
        self.r_message = False
        MenuProfessor.setObjectName("MenuProfessor")
        MenuProfessor.setEnabled(True)
        MenuProfessor.resize(711, 474)
        MenuProfessor.setAutoFillBackground(False)
        MenuProfessor.setAnimated(True)
        MenuProfessor.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MenuProfessor)
        self.centralwidget.setObjectName("centralwidget")
        self.Fundogeral = QtWidgets.QLabel(self.centralwidget)
        self.Fundogeral.setGeometry(QtCore.QRect(0, -40, 791, 531))
        self.Fundogeral.setText("")
        self.Fundogeral.setPixmap(QtGui.QPixmap("../../../../fundo azul.jpg"))
        self.Fundogeral.setScaledContents(True)
        self.Fundogeral.setOpenExternalLinks(False)
        self.Fundogeral.setObjectName("Fundogeral")
        self.Tabelageral = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabelageral.setGeometry(QtCore.QRect(-10, 0, 741, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Tabelageral.setFont(font)
        self.Tabelageral.setStyleSheet("QWidget{\n"
"    color: rgb(3, 0, 117)\n"
"}")
        self.Tabelageral.setObjectName("Tabelageral")
        self.cadastrarprofessor = QtWidgets.QWidget()
        self.cadastrarprofessor.setObjectName("cadastrarprofessor")
        self.fundo = QtWidgets.QLabel(self.cadastrarprofessor)
        self.fundo.setGeometry(QtCore.QRect(-40, -100, 741, 531))
        self.fundo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fundo.setText("")
        self.fundo.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo.setScaledContents(True)
        self.fundo.setObjectName("fundo")
        self.layoutWidget_2 = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 110, 441, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.agrupamento3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.agrupamento3.setContentsMargins(0, 0, 0, 0)
        self.agrupamento3.setObjectName("agrupamento3")
        self.Cpf = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Cpf.setFont(font)
        self.Cpf.setObjectName("Cpf")
        self.agrupamento3.addWidget(self.Cpf)
        self.CampoCpf = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.CampoCpf.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoCpf.setObjectName("CampoCpf")
        self.agrupamento3.addWidget(self.CampoCpf)
        self.layoutWidget_3 = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget_3.setGeometry(QtCore.QRect(90, 190, 441, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.agrupamento4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.agrupamento4.setContentsMargins(0, 0, 0, 0)
        self.agrupamento4.setObjectName("agrupamento4")
        self.Email = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Email.setFont(font)
        self.Email.setObjectName("Email")
        self.agrupamento4.addWidget(self.Email)
        self.CampoEmail = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.CampoEmail.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoEmail.setObjectName("CampoEmail")
        self.agrupamento4.addWidget(self.CampoEmail)
        self.layoutWidget_4 = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget_4.setGeometry(QtCore.QRect(90, 70, 441, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.agrupamento5 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.agrupamento5.setContentsMargins(0, 0, 0, 0)
        self.agrupamento5.setObjectName("agrupamento5")
        self.Siape = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Siape.setFont(font)
        self.Siape.setObjectName("Siape")
        self.agrupamento5.addWidget(self.Siape)
        self.CampoSiape = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.CampoSiape.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoSiape.setObjectName("CampoSiape")
        self.agrupamento5.addWidget(self.CampoSiape)
        self.layoutWidget_5 = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget_5.setGeometry(QtCore.QRect(90, 150, 441, 41))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.agrupamento6 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.agrupamento6.setContentsMargins(0, 0, 0, 0)
        self.agrupamento6.setObjectName("agrupamento6")
        self.Senha = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Senha.setFont(font)
        self.Senha.setObjectName("Senha")
        self.agrupamento6.addWidget(self.Senha)
        self.CampoSenha = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.CampoSenha.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoSenha.setObjectName("CampoSenha")
        self.agrupamento6.addWidget(self.CampoSenha)
        self.layoutWidget_6 = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget_6.setGeometry(QtCore.QRect(90, 230, 441, 41))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.agrupamento7 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.agrupamento7.setContentsMargins(0, 0, 0, 0)
        self.agrupamento7.setObjectName("agrupamento7")
        self.Telefone = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Telefone.setFont(font)
        self.Telefone.setObjectName("Telefone")
        self.agrupamento7.addWidget(self.Telefone)
        self.CampoTelefone = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.CampoTelefone.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoTelefone.setObjectName("CampoTelefone")
        self.agrupamento7.addWidget(self.CampoTelefone)
        self.layoutWidget_7 = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget_7.setGeometry(QtCore.QRect(90, 270, 441, 41))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.Agrupamento8 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.Agrupamento8.setContentsMargins(0, 0, 0, 0)
        self.Agrupamento8.setObjectName("Agrupamento8")
        self.Disciplina = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Disciplina.setFont(font)
        self.Disciplina.setObjectName("Disciplina")
        self.Agrupamento8.addWidget(self.Disciplina)
        self.CampoDisciplina = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.CampoDisciplina.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoDisciplina.setObjectName("CampoDisciplina")
        self.Agrupamento8.addWidget(self.CampoDisciplina)
        self.layoutWidget = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 30, 441, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.agrupamento1 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.agrupamento1.setContentsMargins(0, 0, 0, 0)
        self.agrupamento1.setObjectName("agrupamento1")
        self.Nome = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Nome.setFont(font)
        self.Nome.setObjectName("Nome")
        self.agrupamento1.addWidget(self.Nome)
        self.CampoNome = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoNome.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoNome.setObjectName("CampoNome")
        self.agrupamento1.addWidget(self.CampoNome)
        self.layoutWidget1 = QtWidgets.QWidget(self.cadastrarprofessor)
        self.layoutWidget1.setGeometry(QtCore.QRect(210, 320, 308, 42))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.agrupamento2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.agrupamento2.setContentsMargins(0, 0, 0, 0)
        self.agrupamento2.setObjectName("agrupamento2")
        self.Cadastrar = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cadastrar.setFont(font)
        self.Cadastrar.setObjectName("Cadastrar")
        self.agrupamento2.addWidget(self.Cadastrar)
        spacerItem = QtWidgets.QSpacerItem(108, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.agrupamento2.addItem(spacerItem)
        self.cancelar = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancelar.setFont(font)
        self.cancelar.setObjectName("cancelar")
        self.agrupamento2.addWidget(self.cancelar)
        self.Tabelageral.addTab(self.cadastrarprofessor, "")
        self.ReservarSala = QtWidgets.QWidget()
        self.ReservarSala.setObjectName("ReservarSala")
        self.fundo_2 = QtWidgets.QLabel(self.ReservarSala)
        self.fundo_2.setGeometry(QtCore.QRect(-10, -60, 741, 531))
        self.fundo_2.setText("")
        self.fundo_2.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_2.setScaledContents(True)
        self.fundo_2.setObjectName("fundo_2")
        self.Selecionar = QtWidgets.QPushButton(self.ReservarSala)
        self.Selecionar.setGeometry(QtCore.QRect(280, 210, 87, 29))
        self.Selecionar.setObjectName("Selecionar")
        self.layoutWidget_9 = QtWidgets.QWidget(self.ReservarSala)
        self.layoutWidget_9.setGeometry(QtCore.QRect(20, 10, 381, 144))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.agrupamento9 = QtWidgets.QHBoxLayout()
        self.agrupamento9.setObjectName("agrupamento9")
        self.Bloco = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Bloco.setFont(font)
        self.Bloco.setObjectName("Bloco")
        self.agrupamento9.addWidget(self.Bloco)
        self.CampoBloco = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.CampoBloco.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoBloco.setObjectName("CampoBloco")
        self.agrupamento9.addWidget(self.CampoBloco)
        self.verticalLayout_2.addLayout(self.agrupamento9)
        self.agrupamento11 = QtWidgets.QHBoxLayout()
        self.agrupamento11.setObjectName("agrupamento11")
        self.Sala = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Sala.setFont(font)
        self.Sala.setObjectName("Sala")
        self.agrupamento11.addWidget(self.Sala)
        self.CampoSala = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.CampoSala.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoSala.setObjectName("CampoSala")
        self.agrupamento11.addWidget(self.CampoSala)
        self.verticalLayout_2.addLayout(self.agrupamento11)
        self.agrupamento10 = QtWidgets.QHBoxLayout()
        self.agrupamento10.setObjectName("agrupamento10")
        self.Dia = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dia.setFont(font)
        self.Dia.setObjectName("Dia")
        self.agrupamento10.addWidget(self.Dia)
        self.CampoDIa = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.CampoDIa.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoDIa.setObjectName("CampoDIa")
        self.agrupamento10.addWidget(self.CampoDIa)
        self.verticalLayout_2.addLayout(self.agrupamento10)
        self.agrupamento10_5 = QtWidgets.QHBoxLayout()
        self.agrupamento10_5.setObjectName("agrupamento10_5")
        self.Horario = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Horario.setFont(font)
        self.Horario.setObjectName("Horario")
        self.agrupamento10_5.addWidget(self.Horario)
        self.CampoHorario_3 = QtWidgets.QLineEdit(self.layoutWidget_9)
        self.CampoHorario_3.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoHorario_3.setObjectName("CampoHorario_3")
        self.agrupamento10_5.addWidget(self.CampoHorario_3)
        self.verticalLayout_2.addLayout(self.agrupamento10_5)
        self.tabela = QtWidgets.QTableWidget(self.ReservarSala)
        self.tabela.setGeometry(QtCore.QRect(20, 170, 691, 241))
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
        self.Listar = QtWidgets.QPushButton(self.ReservarSala)
        self.Listar.setGeometry(QtCore.QRect(470, 20, 151, 41))
        self.Listar.setObjectName("Listar")
        self.Reservar = QtWidgets.QPushButton(self.ReservarSala)
        self.Reservar.setGeometry(QtCore.QRect(470, 80, 151, 41))
        self.Reservar.setObjectName("Reservar")
        self.Tabelageral.addTab(self.ReservarSala, "")
        self.Verreservas = QtWidgets.QWidget()
        self.Verreservas.setObjectName("Verreservas")
        self.fundo_3 = QtWidgets.QLabel(self.Verreservas)
        self.fundo_3.setGeometry(QtCore.QRect(-10, 0, 791, 531))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.fundo_3.setFont(font)
        self.fundo_3.setText("")
        self.fundo_3.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_3.setScaledContents(True)
        self.fundo_3.setObjectName("fundo_3")
        self.Mostrar = QtWidgets.QPushButton(self.Verreservas)
        self.Mostrar.setGeometry(QtCore.QRect(220, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mostrar.setFont(font)
        self.Mostrar.setObjectName("Mostrar")
        self.gerarPDF = QtWidgets.QPushButton(self.Verreservas)
        self.gerarPDF.setGeometry(QtCore.QRect(340, 330, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.gerarPDF.setFont(font)
        self.gerarPDF.setObjectName("gerarPDF")
        self.reservas = QtWidgets.QListWidget(self.Verreservas)
        self.reservas.setGeometry(QtCore.QRect(50, 20, 571, 291))
        self.reservas.setObjectName("reservas")
        self.Tabelageral.addTab(self.Verreservas, "")
        self.cancelarreserva = QtWidgets.QWidget()
        self.cancelarreserva.setObjectName("cancelarreserva")
        self.fundo_4 = QtWidgets.QLabel(self.cancelarreserva)
        self.fundo_4.setGeometry(QtCore.QRect(-110, 10, 931, 401))
        self.fundo_4.setText("")
        self.fundo_4.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_4.setObjectName("fundo_4")
        self.Remover = QtWidgets.QPushButton(self.cancelarreserva)
        self.Remover.setGeometry(QtCore.QRect(280, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remover.setFont(font)
        self.Remover.setObjectName("Remover")
        self.layoutWidget_8 = QtWidgets.QWidget(self.cancelarreserva)
        self.layoutWidget_8.setGeometry(QtCore.QRect(170, 90, 321, 131))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.Agrupamento13 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.Agrupamento13.setContentsMargins(0, 0, 0, 0)
        self.Agrupamento13.setObjectName("Agrupamento13")
        self.subagrupamento1 = QtWidgets.QHBoxLayout()
        self.subagrupamento1.setObjectName("subagrupamento1")
        self.Bloco_2 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Bloco_2.setFont(font)
        self.Bloco_2.setObjectName("Bloco_2")
        self.subagrupamento1.addWidget(self.Bloco_2)
        self.CampoBloco_2 = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.CampoBloco_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoBloco_2.setObjectName("CampoBloco_2")
        self.subagrupamento1.addWidget(self.CampoBloco_2)
        self.Agrupamento13.addLayout(self.subagrupamento1)
        self.subagrupamento2 = QtWidgets.QHBoxLayout()
        self.subagrupamento2.setObjectName("subagrupamento2")
        self.Sala_2 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sala_2.setFont(font)
        self.Sala_2.setObjectName("Sala_2")
        self.subagrupamento2.addWidget(self.Sala_2)
        self.CampoSala_2 = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.CampoSala_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoSala_2.setObjectName("CampoSala_2")
        self.subagrupamento2.addWidget(self.CampoSala_2)
        self.Agrupamento13.addLayout(self.subagrupamento2)
        self.subagrupamento3 = QtWidgets.QHBoxLayout()
        self.subagrupamento3.setObjectName("subagrupamento3")
        self.Dia_2 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Dia_2.setFont(font)
        self.Dia_2.setObjectName("Dia_2")
        self.subagrupamento3.addWidget(self.Dia_2)
        self.CampoDia = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.CampoDia.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoDia.setObjectName("CampoDia")
        self.subagrupamento3.addWidget(self.CampoDia)
        self.Agrupamento13.addLayout(self.subagrupamento3)
        self.Tabelageral.addTab(self.cancelarreserva, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.fundo_5 = QtWidgets.QLabel(self.tab)
        self.fundo_5.setGeometry(QtCore.QRect(0, -40, 741, 531))
        self.fundo_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.fundo_5.setText("")
        self.fundo_5.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_5.setScaledContents(True)
        self.fundo_5.setObjectName("fundo_5")
        self.SenhaBotao = QtWidgets.QPushButton(self.tab)
        self.SenhaBotao.setGeometry(QtCore.QRect(240, 80, 171, 41))
        self.SenhaBotao.setObjectName("SenhaBotao")
        self.SenhaBotao_2 = QtWidgets.QPushButton(self.tab)
        self.SenhaBotao_2.setGeometry(QtCore.QRect(240, 130, 171, 41))
        self.SenhaBotao_2.setObjectName("SenhaBotao_2")
        self.SenhaBotao_3 = QtWidgets.QPushButton(self.tab)
        self.SenhaBotao_3.setGeometry(QtCore.QRect(240, 180, 171, 41))
        self.SenhaBotao_3.setObjectName("SenhaBotao_3")
        self.Tabelageral.addTab(self.tab, "")
        MenuProfessor.setCentralWidget(self.centralwidget)
        self.rodape = QtWidgets.QStatusBar(MenuProfessor)
        self.rodape.setObjectName("rodape")
        MenuProfessor.setStatusBar(self.rodape)

        self.retranslateUi(MenuProfessor)
        self.Tabelageral.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MenuProfessor)

    def retranslateUi(self, MenuProfessor):
        _translate = QtCore.QCoreApplication.translate
        MenuProfessor.setWindowTitle(_translate("MenuProfessor", "MENU COORDENADOR"))
        self.Cpf.setText(_translate("MenuProfessor", "CPF               "))
        self.Email.setText(_translate("MenuProfessor", "EMAIL          "))
        self.Siape.setText(_translate("MenuProfessor", "MATRICULA"))
        self.Senha.setText(_translate("MenuProfessor", "SENHA         "))
        self.Telefone.setText(_translate("MenuProfessor", "TELEFONE   "))
        self.Disciplina.setText(_translate("MenuProfessor", "DISCIPLINA"))
        self.Nome.setText(_translate("MenuProfessor", "NOME          "))
        self.Cadastrar.setText(_translate("MenuProfessor", "CADASTRAR"))
        self.cancelar.setText(_translate("MenuProfessor", "CANCELAR"))
        self.Tabelageral.setTabText(self.Tabelageral.indexOf(self.cadastrarprofessor), _translate("MenuProfessor", "Cadastrar Monitor"))
        self.Selecionar.setText(_translate("MenuProfessor", "SELECIONAR"))
        self.Bloco.setText(_translate("MenuProfessor", "BLOCO"))
        self.Sala.setText(_translate("MenuProfessor", "SALA    "))
        self.Dia.setText(_translate("MenuProfessor", "DIA       "))
        self.Horario.setText(_translate("MenuProfessor", "Horário "))
        item = self.tabela.verticalHeaderItem(0)
        item.setText(_translate("MenuProfessor", "8:00 - 10:00"))
        item = self.tabela.verticalHeaderItem(1)
        item.setText(_translate("MenuProfessor", "10:00 - 12:00"))
        item = self.tabela.verticalHeaderItem(2)
        item.setText(_translate("MenuProfessor", "12:00 - 14:00"))
        item = self.tabela.verticalHeaderItem(3)
        item.setText(_translate("MenuProfessor", "14:00 - 16:00"))
        item = self.tabela.verticalHeaderItem(4)
        item.setText(_translate("MenuProfessor", "16:00 - 18:00"))
        item = self.tabela.verticalHeaderItem(5)
        item.setText(_translate("MenuProfessor", "18:00- 20:00"))
        item = self.tabela.verticalHeaderItem(6)
        item.setText(_translate("MenuProfessor", "20:00- 22:00"))
        item = self.tabela.horizontalHeaderItem(0)
        item.setText(_translate("MenuProfessor", "Segunda"))
        item = self.tabela.horizontalHeaderItem(1)
        item.setText(_translate("MenuProfessor", "Terça"))
        item = self.tabela.horizontalHeaderItem(2)
        item.setText(_translate("MenuProfessor", "Quarta"))
        item = self.tabela.horizontalHeaderItem(3)
        item.setText(_translate("MenuProfessor", "Quinta"))
        item = self.tabela.horizontalHeaderItem(4)
        item.setText(_translate("MenuProfessor", "Sexta"))
        item = self.tabela.horizontalHeaderItem(5)
        item.setText(_translate("MenuProfessor", "Sabado"))
        self.Listar.setText(_translate("MenuProfessor", "Listar Horarios"))
        self.Reservar.setText(_translate("MenuProfessor", "Reservar"))
        self.Tabelageral.setTabText(self.Tabelageral.indexOf(self.ReservarSala), _translate("MenuProfessor", "Reservar Sala"))
        self.Mostrar.setText(_translate("MenuProfessor", "MOSTRAR"))
        self.gerarPDF.setText(_translate("MenuProfessor", "GERAR PDF"))
        self.Tabelageral.setTabText(self.Tabelageral.indexOf(self.Verreservas), _translate("MenuProfessor", "Ver reservas"))
        self.Remover.setText(_translate("MenuProfessor", "REMOVER"))
        self.Bloco_2.setText(_translate("MenuProfessor", "BLOCO"))
        self.Sala_2.setText(_translate("MenuProfessor", "SALA    "))
        self.Dia_2.setText(_translate("MenuProfessor", "DIA      "))
        self.Tabelageral.setTabText(self.Tabelageral.indexOf(self.cancelarreserva), _translate("MenuProfessor", "Cancelar reserva"))
        self.SenhaBotao.setText(_translate("MenuProfessor", "SENHA"))
        self.SenhaBotao_2.setText(_translate("MenuProfessor", "EMAIL"))
        self.SenhaBotao_3.setText(_translate("MenuProfessor", "TELEFONE"))
        self.Tabelageral.setTabText(self.Tabelageral.indexOf(self.tab), _translate("MenuProfessor", "Alterar Dados"))
        self.funcionalidade()


    def funcionalidade(self):
        self.Cadastrar.clicked.connect(self.cadastrar)
        self.cancelar.clicked.connect(self.Cancelar)
        
    def mostrar(self):
        print("Nome",self.professor.getNome())
        print("Siape",self.professor.getSIAPE())
        print("Cpf",self.professor.getCpf())
        print("Senha",self.professor.getSenha())
        print("Email:",self.professor.getEmail())
        print("Telefone",self.professor.getTelefone())
        print("Disciplina",self.professor.getDisciplina())
    def cadastrar(self):
        nome=self.CampoNome.text()
        mat= self.CampoSiape.text()
        telefone= self.CampoTelefone.text()
        email= self.CampoEmail.text()
        senha=self.CampoSenha.text()
        cpf= self.CampoCpf.text()
        disciplina= self.CampoDisciplina.text()

        if verificaEmail(email) and verificaCpf(cpf) and verificaTelefone(telefone) and len(nome)> 0 and verificaMat(mat) and len(senha) >0 and len(disciplina)>0:
            string = 'm'+","+nome+","+mat+","+cpf+","+senha+","+email+","+telefone+","+disciplina
            #print(string)
            c1 = cliente(string)
            string2 = c1.client_socket.recv(1024).decode()
            if(string2=="certo"):
                QtWidgets.QMessageBox.about(None, "Cadastro","Cadastro realizado com sucesso!!!",)
                self.CampoNome.clear()
                self.CampoSiape.clear()
                self.CampoTelefone.clear()
                self.CampoEmail.clear()
                self.CampoSenha.clear()
                self.CampoCpf.clear()
                self.CampoDisciplina.clear()
            else:
                QtWidgets.QMessageBox.about(None, "AVISO","Os seguintos dados já estão cadastrados:\n"+string2)
        else:
            QtWidgets.QMessageBox.about(None, "Alguns Valores invalidos","Preencha os campos com valores validos",)

    def Cancelar(self):
        pass
    def loga_professor(self,professor1):
        self.professor = professor1
        if(not self.r_message):
            QtWidgets.QMessageBox.information(None, "AVISO","Bem vindo professor: "+self.professor.getNome(),)
            self.r_message = True
        self.mostrar()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuProfessor = QtWidgets.QMainWindow()
    ui = Ui_MenuProfessor()
    ui.setupUi(MenuProfessor)
    MenuProfessor.show()
    sys.exit(app.exec_())


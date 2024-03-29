# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_tecnico.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from verificaEmail import verificaEmail, verificaCpf, verificaTelefone, verificaMat
from cliente import cliente

class Ui_MenuTecnico(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(642, 502)
        self.r_message = False
        self.tecnico = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fundo = QtWidgets.QLabel(self.centralwidget)
        self.fundo.setGeometry(QtCore.QRect(0, -40, 791, 531))
        self.fundo.setText("")
        self.fundo.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo.setObjectName("fundo")
        self.TabelGeral = QtWidgets.QTabWidget(self.centralwidget)
        self.TabelGeral.setGeometry(QtCore.QRect(0, 0, 741, 461))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TabelGeral.setFont(font)
        self.TabelGeral.setStyleSheet("QWidget{\n"
"    color: rgb(3, 0, 117)\n"
"}")
        self.TabelGeral.setObjectName("TabelGeral")
        self.CadastrarCoordenador = QtWidgets.QWidget()
        self.CadastrarCoordenador.setObjectName("CadastrarCoordenador")
        self.fundo_3 = QtWidgets.QLabel(self.CadastrarCoordenador)
        self.fundo_3.setGeometry(QtCore.QRect(-10, -60, 741, 531))
        self.fundo_3.setText("")
        self.fundo_3.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_3.setObjectName("fundo_3")
        self.layoutWidget = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 10, 441, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.agrupamento = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.agrupamento.setContentsMargins(0, 0, 0, 0)
        self.agrupamento.setObjectName("agrupamento")
        self.Nome = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Nome.setFont(font)
        self.Nome.setObjectName("Nome")
        self.agrupamento.addWidget(self.Nome)
        self.CampoNome = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoNome.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoNome.setObjectName("CampoNome")
        self.agrupamento.addWidget(self.CampoNome)
        self.layoutWidget_3 = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget_3.setGeometry(QtCore.QRect(100, 90, 441, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.agrupamento_2 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.agrupamento_2.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_2.setObjectName("agrupamento_2")
        self.cpf = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cpf.setFont(font)
        self.cpf.setObjectName("cpf")
        self.agrupamento_2.addWidget(self.cpf)
        self.CampoCpf = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.CampoCpf.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoCpf.setObjectName("CampoCpf")
        self.agrupamento_2.addWidget(self.CampoCpf)
        self.layoutWidget_6 = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget_6.setGeometry(QtCore.QRect(100, 210, 441, 41))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.agrupamento_5 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.agrupamento_5.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_5.setObjectName("agrupamento_5")
        self.Telefone = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Telefone.setFont(font)
        self.Telefone.setObjectName("Telefone")
        self.agrupamento_5.addWidget(self.Telefone)
        self.CampoTelefone = QtWidgets.QLineEdit(self.layoutWidget_6)
        self.CampoTelefone.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoTelefone.setObjectName("CampoTelefone")
        self.agrupamento_5.addWidget(self.CampoTelefone)
        self.layoutWidget_7 = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget_7.setGeometry(QtCore.QRect(100, 250, 441, 41))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.agrupamento_6 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.agrupamento_6.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_6.setObjectName("agrupamento_6")
        self.disciplina = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.disciplina.setFont(font)
        self.disciplina.setObjectName("disciplina")
        self.agrupamento_6.addWidget(self.disciplina)
        self.CampoDisciplina = QtWidgets.QLineEdit(self.layoutWidget_7)
        self.CampoDisciplina.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoDisciplina.setObjectName("CampoDisciplina")
        self.agrupamento_6.addWidget(self.CampoDisciplina)
        self.layoutWidget_5 = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget_5.setGeometry(QtCore.QRect(100, 130, 441, 41))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.agrupamento_4 = QtWidgets.QHBoxLayout(self.layoutWidget_5)
        self.agrupamento_4.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_4.setObjectName("agrupamento_4")
        self.Senha = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Senha.setFont(font)
        self.Senha.setObjectName("Senha")
        self.agrupamento_4.addWidget(self.Senha)
        self.CampoSenha = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.CampoSenha.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoSenha.setObjectName("CampoSenha")
        self.agrupamento_4.addWidget(self.CampoSenha)
        self.layoutWidget_4 = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget_4.setGeometry(QtCore.QRect(100, 50, 441, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.agrupamento_3 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.agrupamento_3.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_3.setObjectName("agrupamento_3")
        self.siape = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.siape.setFont(font)
        self.siape.setObjectName("siape")
        self.agrupamento_3.addWidget(self.siape)
        self.CampoSiape = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.CampoSiape.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoSiape.setObjectName("CampoSiape")
        self.agrupamento_3.addWidget(self.CampoSiape)
        self.layoutWidget_8 = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget_8.setGeometry(QtCore.QRect(100, 170, 441, 41))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.agrupamento_7 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.agrupamento_7.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_7.setObjectName("agrupamento_7")
        self.email = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.agrupamento_7.addWidget(self.email)
        self.CampoEmail = QtWidgets.QLineEdit(self.layoutWidget_8)
        self.CampoEmail.setStyleSheet("QLineEdit{\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.CampoEmail.setObjectName("CampoEmail")
        self.agrupamento_7.addWidget(self.CampoEmail)
        self.layoutWidget_9 = QtWidgets.QWidget(self.CadastrarCoordenador)
        self.layoutWidget_9.setGeometry(QtCore.QRect(210, 300, 308, 42))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.agrupamento_8 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.agrupamento_8.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_8.setObjectName("agrupamento_8")
        self.cadastrar = QtWidgets.QPushButton(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cadastrar.setFont(font)
        self.cadastrar.setObjectName("cadastrar")
        self.agrupamento_8.addWidget(self.cadastrar)
        spacerItem = QtWidgets.QSpacerItem(108, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.agrupamento_8.addItem(spacerItem)
        self.cancelar = QtWidgets.QPushButton(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancelar.setFont(font)
        self.cancelar.setObjectName("cancelar")
        self.agrupamento_8.addWidget(self.cancelar)
        self.TabelGeral.addTab(self.CadastrarCoordenador, "")
        self.reservas_2 = QtWidgets.QWidget()
        self.reservas_2.setObjectName("reservas_2")
        self.fundo_4 = QtWidgets.QLabel(self.reservas_2)
        self.fundo_4.setGeometry(QtCore.QRect(-10, 0, 791, 531))
        self.fundo_4.setText("")
        self.fundo_4.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_4.setObjectName("fundo_4")
        self.listagem = QtWidgets.QListView(self.reservas_2)
        self.listagem.setGeometry(QtCore.QRect(50, 30, 601, 281))
        self.listagem.setObjectName("listagem")
        self.mostrar = QtWidgets.QPushButton(self.reservas_2)
        self.mostrar.setGeometry(QtCore.QRect(240, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mostrar.setFont(font)
        self.mostrar.setObjectName("mostrar")
        self.GerarPDF = QtWidgets.QPushButton(self.reservas_2)
        self.GerarPDF.setGeometry(QtCore.QRect(350, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.GerarPDF.setFont(font)
        self.GerarPDF.setObjectName("GerarPDF")
        self.TabelGeral.addTab(self.reservas_2, "")
        self.CancelarReserva = QtWidgets.QWidget()
        self.CancelarReserva.setObjectName("CancelarReserva")
        self.fundo_5 = QtWidgets.QLabel(self.CancelarReserva)
        self.fundo_5.setGeometry(QtCore.QRect(-20, -10, 791, 531))
        self.fundo_5.setText("")
        self.fundo_5.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_5.setObjectName("fundo_5")
        self.layoutWidget_2 = QtWidgets.QWidget(self.CancelarReserva)
        self.layoutWidget_2.setGeometry(QtCore.QRect(150, 90, 331, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.agrupamento_9 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.agrupamento_9.setContentsMargins(0, 0, 0, 0)
        self.agrupamento_9.setObjectName("agrupamento_9")
        self.agrupamento_10 = QtWidgets.QHBoxLayout()
        self.agrupamento_10.setObjectName("agrupamento_10")
        self.bloco = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bloco.setFont(font)
        self.bloco.setObjectName("bloco")
        self.agrupamento_10.addWidget(self.bloco)
        self.CampoBloco = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.CampoBloco.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoBloco.setObjectName("CampoBloco")
        self.agrupamento_10.addWidget(self.CampoBloco)
        self.agrupamento_9.addLayout(self.agrupamento_10)
        self.agrupamento_11 = QtWidgets.QHBoxLayout()
        self.agrupamento_11.setObjectName("agrupamento_11")
        self.Sala = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Sala.setFont(font)
        self.Sala.setObjectName("Sala")
        self.agrupamento_11.addWidget(self.Sala)
        self.CampoSala = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.CampoSala.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoSala.setObjectName("CampoSala")
        self.agrupamento_11.addWidget(self.CampoSala)
        self.agrupamento_9.addLayout(self.agrupamento_11)
        self.agrupamento_12 = QtWidgets.QHBoxLayout()
        self.agrupamento_12.setObjectName("agrupamento_12")
        self.Dia = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Dia.setFont(font)
        self.Dia.setObjectName("Dia")
        self.agrupamento_12.addWidget(self.Dia)
        self.CampoDIa = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.CampoDIa.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoDIa.setObjectName("CampoDIa")
        self.agrupamento_12.addWidget(self.CampoDIa)
        self.agrupamento_9.addLayout(self.agrupamento_12)
        self.remover = QtWidgets.QPushButton(self.CancelarReserva)
        self.remover.setGeometry(QtCore.QRect(260, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.remover.setFont(font)
        self.remover.setObjectName("remover")
        self.layoutWidget_13 = QtWidgets.QWidget(self.CancelarReserva)
        self.layoutWidget_13.setGeometry(QtCore.QRect(150, 60, 331, 31))
        self.layoutWidget_13.setObjectName("layoutWidget_13")
        self.subagrupamento4_2 = QtWidgets.QHBoxLayout(self.layoutWidget_13)
        self.subagrupamento4_2.setContentsMargins(0, 0, 0, 0)
        self.subagrupamento4_2.setObjectName("subagrupamento4_2")
        self.SIAPE_2 = QtWidgets.QLabel(self.layoutWidget_13)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SIAPE_2.setFont(font)
        self.SIAPE_2.setObjectName("SIAPE_2")
        self.subagrupamento4_2.addWidget(self.SIAPE_2)
        self.CampoSIAPE_2 = QtWidgets.QLineEdit(self.layoutWidget_13)
        self.CampoSIAPE_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoSIAPE_2.setObjectName("CampoSIAPE_2")
        self.subagrupamento4_2.addWidget(self.CampoSIAPE_2)
        self.TabelGeral.addTab(self.CancelarReserva, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.fundo_6 = QtWidgets.QLabel(self.tab)
        self.fundo_6.setGeometry(QtCore.QRect(-30, -20, 791, 531))
        self.fundo_6.setText("")
        self.fundo_6.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_6.setObjectName("fundo_6")
        self.SenhaBotao_2 = QtWidgets.QPushButton(self.tab)
        self.SenhaBotao_2.setGeometry(QtCore.QRect(260, 140, 171, 41))
        self.SenhaBotao_2.setObjectName("SenhaBotao_2")
        self.SenhaBotao_3 = QtWidgets.QPushButton(self.tab)
        self.SenhaBotao_3.setGeometry(QtCore.QRect(260, 190, 171, 41))
        self.SenhaBotao_3.setObjectName("SenhaBotao_3")
        self.SenhaBotao = QtWidgets.QPushButton(self.tab)
        self.SenhaBotao.setGeometry(QtCore.QRect(260, 90, 171, 41))
        self.SenhaBotao.setObjectName("SenhaBotao")
        self.TabelGeral.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.fundo_7 = QtWidgets.QLabel(self.tab_2)
        self.fundo_7.setGeometry(QtCore.QRect(-100, -20, 791, 531))
        self.fundo_7.setText("")
        self.fundo_7.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_7.setObjectName("fundo_7")
        self.layoutWidget_10 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_10.setGeometry(QtCore.QRect(110, 130, 391, 31))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bloco_2 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bloco_2.setFont(font)
        self.bloco_2.setObjectName("bloco_2")
        self.horizontalLayout.addWidget(self.bloco_2)
        self.CampoBloco_2 = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.CampoBloco_2.setObjectName("CampoBloco_2")
        self.horizontalLayout.addWidget(self.CampoBloco_2)
        self.cadastrar_2 = QtWidgets.QPushButton(self.tab_2)
        self.cadastrar_2.setGeometry(QtCore.QRect(250, 230, 87, 29))
        self.cadastrar_2.setObjectName("cadastrar_2")
        self.layoutWidget_11 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_11.setGeometry(QtCore.QRect(110, 170, 391, 31))
        self.layoutWidget_11.setObjectName("layoutWidget_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_11)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sala = QtWidgets.QLabel(self.layoutWidget_11)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sala.setFont(font)
        self.sala.setObjectName("sala")
        self.horizontalLayout_2.addWidget(self.sala)
        self.CampoSala_2 = QtWidgets.QLineEdit(self.layoutWidget_11)
        self.CampoSala_2.setObjectName("CampoSala_2")
        self.horizontalLayout_2.addWidget(self.CampoSala_2)
        self.TabelGeral.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.fundo_8 = QtWidgets.QLabel(self.tab_3)
        self.fundo_8.setGeometry(QtCore.QRect(-130, -60, 791, 531))
        self.fundo_8.setText("")
        self.fundo_8.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_8.setObjectName("fundo_8")
        self.layoutWidget_12 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_12.setGeometry(QtCore.QRect(120, 200, 461, 36))
        self.layoutWidget_12.setObjectName("layoutWidget_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_12)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Siape_2 = QtWidgets.QLabel(self.layoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Siape_2.setFont(font)
        self.Siape_2.setObjectName("Siape_2")
        self.horizontalLayout_4.addWidget(self.Siape_2)
        self.LabelSiape = QtWidgets.QLabel(self.layoutWidget_12)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabelSiape.setFont(font)
        self.LabelSiape.setText("")
        self.LabelSiape.setObjectName("LabelSiape")
        self.horizontalLayout_4.addWidget(self.LabelSiape)
        self.layoutWidget_14 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_14.setGeometry(QtCore.QRect(120, 120, 461, 36))
        self.layoutWidget_14.setObjectName("layoutWidget_14")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_14)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.nome = QtWidgets.QLabel(self.layoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nome.setFont(font)
        self.nome.setObjectName("nome")
        self.horizontalLayout_5.addWidget(self.nome)
        self.LabelNome = QtWidgets.QLabel(self.layoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabelNome.setFont(font)
        self.LabelNome.setText("")
        self.LabelNome.setObjectName("LabelNome")
        self.horizontalLayout_5.addWidget(self.LabelNome)
        self.layoutWidget_15 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_15.setGeometry(QtCore.QRect(120, 160, 461, 36))
        self.layoutWidget_15.setObjectName("layoutWidget_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_15)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.email_2 = QtWidgets.QLabel(self.layoutWidget_15)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.email_2.setFont(font)
        self.email_2.setObjectName("email_2")
        self.horizontalLayout_6.addWidget(self.email_2)
        self.LabeEmail = QtWidgets.QLabel(self.layoutWidget_15)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabeEmail.setFont(font)
        self.LabeEmail.setText("")
        self.LabeEmail.setObjectName("LabeEmail")
        self.horizontalLayout_6.addWidget(self.LabeEmail)
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget1.setGeometry(QtCore.QRect(120, 80, 461, 36))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.Telefone_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.Telefone_2.setFont(font)
        self.Telefone_2.setObjectName("Telefone_2")
        self.horizontalLayout_7.addWidget(self.Telefone_2)
        self.LabelTelefone = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.LabelTelefone.setFont(font)
        self.LabelTelefone.setText("")
        self.LabelTelefone.setObjectName("LabelTelefone")
        self.horizontalLayout_7.addWidget(self.LabelTelefone)
        self.TabelGeral.addTab(self.tab_3, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabelGeral.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MENU TECNICO"))
        self.Nome.setText(_translate("MainWindow", "NOME          "))
        self.cpf.setText(_translate("MainWindow", "CPF               "))
        self.Telefone.setText(_translate("MainWindow", "TELEFONE   "))
        self.disciplina.setText(_translate("MainWindow", "DISCIPLINA"))
        self.Senha.setText(_translate("MainWindow", "SENHA         "))
        self.siape.setText(_translate("MainWindow", "SIAPE           "))
        self.email.setText(_translate("MainWindow", "EMAIL          "))
        self.cadastrar.setText(_translate("MainWindow", "CADASTRAR"))
        self.cancelar.setText(_translate("MainWindow", "CANCELAR"))
        self.TabelGeral.setTabText(self.TabelGeral.indexOf(self.CadastrarCoordenador), _translate("MainWindow", "Cadastrar Coordenador"))
        self.mostrar.setText(_translate("MainWindow", "MOSTRAR"))
        self.GerarPDF.setText(_translate("MainWindow", "Gerar  PDF"))
        self.TabelGeral.setTabText(self.TabelGeral.indexOf(self.reservas_2), _translate("MainWindow", "Ver reservas"))
        self.bloco.setText(_translate("MainWindow", "BLOCO"))
        self.Sala.setText(_translate("MainWindow", "SALA    "))
        self.Dia.setText(_translate("MainWindow", "DIA      "))
        self.remover.setText(_translate("MainWindow", "REMOVER"))
        self.SIAPE_2.setText(_translate("MainWindow", "HORARIO  "))
        self.TabelGeral.setTabText(self.TabelGeral.indexOf(self.CancelarReserva), _translate("MainWindow", "Cancelar reserva"))
        self.SenhaBotao_2.setText(_translate("MainWindow", "EMAIL"))
        self.SenhaBotao_3.setText(_translate("MainWindow", "TELEFONE"))
        self.SenhaBotao.setText(_translate("MainWindow", "SENHA"))
        self.TabelGeral.setTabText(self.TabelGeral.indexOf(self.tab), _translate("MainWindow", "Alterar Dados"))
        self.bloco_2.setText(_translate("MainWindow", "BLOCO"))
        self.cadastrar_2.setText(_translate("MainWindow", "Cadastrar"))
        self.sala.setText(_translate("MainWindow", "SALA    "))
        self.TabelGeral.setTabText(self.TabelGeral.indexOf(self.tab_2), _translate("MainWindow", "Cadastrar Bloco"))
        self.Siape_2.setText(_translate("MainWindow", "SIAPE"))
        self.nome.setText(_translate("MainWindow", "NOME"))
        self.email_2.setText(_translate("MainWindow", "EMAIL"))
        self.Telefone_2.setText(_translate("MainWindow", "TELEFONE:"))
        self.TabelGeral.setTabText(self.TabelGeral.indexOf(self.tab_3), _translate("MainWindow", "Informações"))


        self.funcionalidade()


    def funcionalidade(self):
        self.cadastrar.clicked.connect(self.cadastra)
        self.cadastrar_2.clicked.connect(self.cadastra_sala)
        self.remover.clicked.connect(self.cancela_reserva_tec)
    def cadastra(self):
        nome=self.CampoNome.text()
        siape= self.CampoSiape.text()
        telefone= self.CampoTelefone.text()
        email= self.CampoEmail.text()
        senha=self.CampoSenha.text()
        cpf= self.CampoCpf.text()
        disciplina= self.CampoDisciplina.text()

        if verificaEmail(email) and verificaCpf(cpf) and verificaTelefone(telefone) and len(nome)> 0 and verificaMat(siape) and len(senha) >0 and len(disciplina)>0:
            string = 'c'+","+nome+","+siape+","+cpf+","+senha+","+email+","+telefone+","+disciplina
            c1 = cliente(string)
            string2 = c1.client_socket.recv(1024).decode()
            
            #print("STRING2",string2)
            #print(string)
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
                QtWidgets.QMessageBox.about(None, "AVISO","Os seguintos dados já estão cadastrados:\n"+string2[:len(string2)-1:1])
        else:
            QtWidgets.QMessageBox.about(None, "Alguns Valores invalidos","Preencha os campos com valores validos",)

    def mostrar1(self):
        print("Nome",self.tecnico.getNome())
        print("Cpf",self.tecnico.getCpf())
        print("Senha",self.tecnico.getSenha())
        print("Email:",self.tecnico.getEmail())
        print("Telefone",self.tecnico.getTelefone())
    def loga_tecnico(self,tec):
        self.tecnico = tec
        if(not self.r_message):
            QtWidgets.QMessageBox.information(None, "AVISO","Bem vindo tecnico: "+self.tecnico.getNome(),)
            self.r_message = True
        self.mostrar1()

    def cadastra_sala(self):
        #self.CampoBloco_2.setText("teste")
        #self.CampoSala_2.setText("ok")
        string = ''
        if(len(self.CampoBloco_2.text())==0 or len(self.CampoSala_2.text())==0):
            QtWidgets.QMessageBox.warning(None, "AVISO","PREENCHA TODOS OS CAMPOS!")
            
        else:
            string = "cad_sala"+","+self.CampoBloco_2.text()+","+self.CampoSala_2.text()
            c1 = cliente(string)
            string2 = c1.client_socket.recv(1024).decode()
            if(string2=="cadastrou"):
                 QtWidgets.QMessageBox.information(None, "AVISO","cadastro de Sala feito com sucesso")
                 self.CampoSala_2.clear()
                 self.CampoBloco_2.clear()
                 
            else:
                QtWidgets.QMessageBox.warning(None, "AVISO","Não foi possivel realizar cadastro")

    def cancela_reserva_tec(self):
        bloco = self.CampoBloco.text()
        sala = self.CampoSala.text()
        dia = self.CampoDIa.text()
        horario = self.CampoSIAPE_2.text()
        string = ''
       
    
        if(len(dia)== 0 or len(sala) == 0 or len(bloco)==0 or len(horario)==0):
            QtWidgets.QMessageBox.information(None, "AVISO","PREENCHA TODOS OS CAMPOS!",)
        else:
            string = "cancelar_reserva_tec"+","+bloco+","+sala+","+dia+","+horario
            c1 = cliente(string)
            string2 = c1.client_socket.recv(1024).decode()
           
            if(string2=="cancelar"):
                QtWidgets.QMessageBox.information(None, "AVISO","Reserva cancelada com sucesso",)
                bloco = self.CampoBloco.clear()
                sala = self.CampoSala.clear()
                dia = self.CampoDIa.clear()
                horario = self.CampoSIAPE_2.clear()
            else:
                QtWidgets.QMessageBox.warning(None, "AVISO","Não há reservas para serem canceladas",)
    

                 
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuTecnico()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tela_Monitor.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuMonitor(object):
    def setupUi(self, MainWindow):
        self.monitor = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(711, 429)
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
        self.Selecionar = QtWidgets.QPushButton(self.ReservaSala)
        self.Selecionar.setGeometry(QtCore.QRect(290, 200, 87, 29))
        self.Selecionar.setObjectName("Selecionar")
        self.layoutWidget = QtWidgets.QWidget(self.ReservaSala)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 80, 421, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.agrupamento9_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.agrupamento9_2.setContentsMargins(0, 0, 0, 0)
        self.agrupamento9_2.setObjectName("agrupamento9_2")
        self.Bloco_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Bloco_2.setFont(font)
        self.Bloco_2.setObjectName("Bloco_2")
        self.agrupamento9_2.addWidget(self.Bloco_2)
        self.CampoBloco_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoBloco_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoBloco_2.setObjectName("CampoBloco_2")
        self.agrupamento9_2.addWidget(self.CampoBloco_2)
        self.layoutWidget_10 = QtWidgets.QWidget(self.ReservaSala)
        self.layoutWidget_10.setGeometry(QtCore.QRect(110, 140, 421, 31))
        self.layoutWidget_10.setObjectName("layoutWidget_10")
        self.agrupamento10_2 = QtWidgets.QHBoxLayout(self.layoutWidget_10)
        self.agrupamento10_2.setContentsMargins(0, 0, 0, 0)
        self.agrupamento10_2.setObjectName("agrupamento10_2")
        self.Dia_2 = QtWidgets.QLabel(self.layoutWidget_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Dia_2.setFont(font)
        self.Dia_2.setObjectName("Dia_2")
        self.agrupamento10_2.addWidget(self.Dia_2)
        self.CampoDIa_2 = QtWidgets.QLineEdit(self.layoutWidget_10)
        self.CampoDIa_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoDIa_2.setObjectName("CampoDIa_2")
        self.agrupamento10_2.addWidget(self.CampoDIa_2)
        self.layoutWidget_9 = QtWidgets.QWidget(self.ReservaSala)
        self.layoutWidget_9.setGeometry(QtCore.QRect(110, 110, 421, 31))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.agrupamento11 = QtWidgets.QHBoxLayout(self.layoutWidget_9)
        self.agrupamento11.setContentsMargins(0, 0, 0, 0)
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
        self.listagem = QtWidgets.QListView(self.VerReservas)
        self.listagem.setGeometry(QtCore.QRect(60, 30, 601, 281))
        self.listagem.setObjectName("listagem")
        self.Mostrar = QtWidgets.QPushButton(self.VerReservas)
        self.Mostrar.setGeometry(QtCore.QRect(310, 320, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Mostrar.setFont(font)
        self.Mostrar.setObjectName("Mostrar")
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
        self.Remover.setGeometry(QtCore.QRect(260, 230, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remover.setFont(font)
        self.Remover.setObjectName("Remover")
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.TabelaGeral.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MENU MONITOR"))
        self.Selecionar.setText(_translate("MainWindow", "SELECIONAR"))
        self.Bloco_2.setText(_translate("MainWindow", "BLOCO"))
        self.Dia_2.setText(_translate("MainWindow", "DIA       "))
        self.Sala.setText(_translate("MainWindow", "SALA    "))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.ReservaSala), _translate("MainWindow", "Reservar Sala"))
        self.Mostrar.setText(_translate("MainWindow", "MOSTRAR"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.VerReservas), _translate("MainWindow", "Ver reservas"))
        self.Bloco_4.setText(_translate("MainWindow", "BLOCO"))
        self.Sala_3.setText(_translate("MainWindow", "SALA    "))
        self.Dia_4.setText(_translate("MainWindow", "DIA      "))
        self.Remover.setText(_translate("MainWindow", "REMOVER"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.CancelarReservas), _translate("MainWindow", "Cancelar reserva"))
        self.EmailBotao.setText(_translate("MainWindow", "EMAIL"))
        self.SenhaBotao.setText(_translate("MainWindow", "SENHA"))
        self.TelefoneBotao.setText(_translate("MainWindow", "TELEFONE"))
        self.CancelarBotao.setText(_translate("MainWindow", "CANCELAR"))
        self.TabelaGeral.setTabText(self.TabelaGeral.indexOf(self.tab), _translate("MainWindow", "Alterar Dados"))
    def mostrar(self):
        print("Nome",self.monitor.getNome())
        print("Siape",self.monitor.getMatricula())
        print("Cpf",self.monitor.getCpf())
        print("Senha",self.monitor.getSenha())
        print("Email:",self.monitor.getEmail())
        print("Telefone",self.monitor.getTelefone())
        print("Matricula",self.monitor.getDisciplina())
        
    def loga_monitor(self,monitor1):
        self.monitor = monitor1
        QtWidgets.QMessageBox.information(None, "AVISO","Bem vindo monitor: "+self.monitor.getNome(),)
        self.mostrar()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MenuMonitor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlterarTelefone.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AlterarTELEFONE(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 468)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fundp = QtWidgets.QLabel(self.centralwidget)
        self.fundp.setGeometry(QtCore.QRect(-40, 0, 801, 531))
        self.fundp.setText("")
        self.fundp.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundp.setObjectName("fundp")
        self.Titulo = QtWidgets.QLabel(self.centralwidget)
        self.Titulo.setGeometry(QtCore.QRect(140, 30, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.Titulo.setFont(font)
        self.Titulo.setStyleSheet("Qlabel{\n"
"    color: blue;\n"
"}")
        self.Titulo.setObjectName("Titulo")
        self.Cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.Cancelar.setGeometry(QtCore.QRect(380, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cancelar.setFont(font)
        self.Cancelar.setObjectName("Cancelar")
        self.Alterar = QtWidgets.QPushButton(self.centralwidget)
        self.Alterar.setGeometry(QtCore.QRect(260, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Alterar.setFont(font)
        self.Alterar.setObjectName("Alterar")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(90, 140, 441, 31))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.agrupamento = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.agrupamento.setContentsMargins(0, 0, 0, 0)
        self.agrupamento.setObjectName("agrupamento")
        self.NovoTelefone = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NovoTelefone.setFont(font)
        self.NovoTelefone.setStyleSheet("Qlabel{\n"
"    color: blue;\n"
"}")
        self.NovoTelefone.setObjectName("NovoTelefone")
        self.agrupamento.addWidget(self.NovoTelefone)
        self.CampoTelefone = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.CampoTelefone.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoTelefone.setObjectName("CampoTelefone")
        self.agrupamento.addWidget(self.CampoTelefone)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Titulo.setText(_translate("MainWindow", "ALTERAR TELEFONE"))
        self.Cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.Alterar.setText(_translate("MainWindow", "Alterar"))
        self.NovoTelefone.setText(_translate("MainWindow", "Novo Telefone"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AlterarTELEFONE()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


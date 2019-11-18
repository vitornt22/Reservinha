# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'redefinirsenha.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RedefinirSenha(object):
    def setupUi(self, RedefinirSenha):
        self.pessoa = None
        RedefinirSenha.setObjectName("RedefinirSenha")
        RedefinirSenha.resize(718, 493)
        self.centralwidget = QtWidgets.QWidget(RedefinirSenha)
        self.centralwidget.setObjectName("centralwidget")
        self.FundoGeral = QtWidgets.QLabel(self.centralwidget)
        self.FundoGeral.setGeometry(QtCore.QRect(-70, -40, 881, 601))
        self.FundoGeral.setText("")
        self.FundoGeral.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.FundoGeral.setObjectName("FundoGeral")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 190, 381, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Agrupamento2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Agrupamento2.setContentsMargins(0, 0, 0, 0)
        self.Agrupamento2.setObjectName("Agrupamento2")
        self.Cofnirmar = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cofnirmar.setFont(font)
        self.Cofnirmar.setObjectName("Cofnirmar")
        self.Agrupamento2.addWidget(self.Cofnirmar)
        self.CampoConfirmar = QtWidgets.QLineEdit(self.layoutWidget)
        self.CampoConfirmar.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoConfirmar.setObjectName("CampoConfirmar")
        self.Agrupamento2.addWidget(self.CampoConfirmar)
        self.Redefinir = QtWidgets.QPushButton(self.centralwidget)
        self.Redefinir.setGeometry(QtCore.QRect(250, 250, 87, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Redefinir.setFont(font)
        self.Redefinir.setObjectName("Redefinir")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(150, 150, 381, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.Agrupamento1 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.Agrupamento1.setContentsMargins(0, 0, 0, 0)
        self.Agrupamento1.setObjectName("Agrupamento1")
        self.NovaSenha = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.NovaSenha.setFont(font)
        self.NovaSenha.setObjectName("NovaSenha")
        self.Agrupamento1.addWidget(self.NovaSenha)
        self.CampoNovaSenha = QtWidgets.QLineEdit(self.layoutWidget1)
        self.CampoNovaSenha.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoNovaSenha.setObjectName("CampoNovaSenha")
        self.Agrupamento1.addWidget(self.CampoNovaSenha)
        self.Cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.Cancelar.setGeometry(QtCore.QRect(420, 250, 87, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cancelar.setFont(font)
        self.Cancelar.setObjectName("Cancelar")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(150, 110, 381, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.agrupamento3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.agrupamento3.setContentsMargins(0, 0, 0, 0)
        self.agrupamento3.setObjectName("agrupamento3")
        self.SenhaAntiga = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SenhaAntiga.setFont(font)
        self.SenhaAntiga.setObjectName("SenhaAntiga")
        self.agrupamento3.addWidget(self.SenhaAntiga)
        self.CampoSenhaAntiga = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.CampoSenhaAntiga.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.CampoSenhaAntiga.setObjectName("CampoSenhaAntiga")
        self.agrupamento3.addWidget(self.CampoSenhaAntiga)
        RedefinirSenha.setCentralWidget(self.centralwidget)
        self.Rodape = QtWidgets.QStatusBar(RedefinirSenha)
        self.Rodape.setObjectName("Rodape")
        RedefinirSenha.setStatusBar(self.Rodape)

        self.retranslateUi(RedefinirSenha)
        QtCore.QMetaObject.connectSlotsByName(RedefinirSenha)

    def retranslateUi(self, RedefinirSenha):
        _translate = QtCore.QCoreApplication.translate
        RedefinirSenha.setWindowTitle(_translate("RedefinirSenha", "MainWindow"))
        self.Cofnirmar.setText(_translate("RedefinirSenha", "CONFIRMAR    "))
        self.Redefinir.setText(_translate("RedefinirSenha", "REDEFINIR"))
        self.NovaSenha.setText(_translate("RedefinirSenha", "NOVA SENHA   "))
        self.Cancelar.setText(_translate("RedefinirSenha", "CANCELAR"))
        self.SenhaAntiga.setText(_translate("RedefinirSenha", "SENHA ANTIGA"))

    def getPessoa(self,pessoa):
        self.pessoa = pessoa
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RedefinirSenha = QtWidgets.QMainWindow()
    ui = Ui_RedefinirSenha()
    ui.setupUi(RedefinirSenha)
    RedefinirSenha.show()
    sys.exit(app.exec_())


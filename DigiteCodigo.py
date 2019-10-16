from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 427)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fundoazul = QtWidgets.QLabel(self.centralwidget)
        self.fundoazul.setGeometry(QtCore.QRect(-37, -4, 781, 481))
        self.fundoazul.setText("")
        self.fundoazul.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundoazul.setObjectName("fundoazul")
        self.LineCodigo = QtWidgets.QLineEdit(self.centralwidget)
        self.LineCodigo.setGeometry(QtCore.QRect(180, 120, 301, 41))
        self.LineCodigo.setStyleSheet("QLineEdit{\n""    background-color: white;\n""}")
        self.LineCodigo.setText("")
        self.LineCodigo.setObjectName("LineCodigo")
        self.Codigo = QtWidgets.QLabel(self.centralwidget)
        self.Codigo.setGeometry(QtCore.QRect(100, 130, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Codigo.setFont(font)
        self.Codigo.setObjectName("Codigo")
        self.confimarCodigo = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.confimarCodigo.setGeometry(QtCore.QRect(230, 170, 241, 41))
        self.confimarCodigo.setStyleSheet("QCommandLinkButton{\n""    color: blue;\n""}")
        self.confimarCodigo.setObjectName("confimarCodigo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.rodape = QtWidgets.QStatusBar(MainWindow)
        self.rodape.setObjectName("rodape")
        MainWindow.setStatusBar(self.rodape)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Redefinir Senha"))
        self.Codigo.setText(_translate("MainWindow", "CÓDIGO"))
        self.confimarCodigo.setText(_translate("MainWindow", "Confirmar código"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


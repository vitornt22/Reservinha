# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AlterarEmail.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AlterarEMAIL(object):
    def setupUi(self, AlterarEMAIL):
        
        AlterarEMAIL.setObjectName("AlterarEMAIL")
        AlterarEMAIL.resize(653, 461)
        self.centralwidget = QtWidgets.QWidget(AlterarEMAIL)
        self.centralwidget.setObjectName("centralwidget")
        self.fundo_4 = QtWidgets.QLabel(self.centralwidget)
        self.fundo_4.setGeometry(QtCore.QRect(-360, -80, 1231, 521))
        self.fundo_4.setText("")
        self.fundo_4.setPixmap(QtGui.QPixmap("../fundo azul.jpg"))
        self.fundo_4.setObjectName("fundo_4")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 190, 441, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("Qlabel{\n"
"    color: blue;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.Remover = QtWidgets.QPushButton(self.centralwidget)
        self.Remover.setGeometry(QtCore.QRect(250, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remover.setFont(font)
        self.Remover.setObjectName("Remover")
        self.Remover_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Remover_2.setGeometry(QtCore.QRect(370, 250, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Remover_2.setFont(font)
        self.Remover_2.setObjectName("Remover_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 60, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("Qlabel{\n"
"    color: blue;\n"
"}")
        self.label_3.setObjectName("label_3")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(100, 160, 441, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("Qlabel{\n"
"    color: blue;\n"
"}")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: white;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        AlterarEMAIL.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AlterarEMAIL)
        self.statusbar.setObjectName("statusbar")
        AlterarEMAIL.setStatusBar(self.statusbar)

        self.retranslateUi(AlterarEMAIL)
        QtCore.QMetaObject.connectSlotsByName(AlterarEMAIL)

    def retranslateUi(self, AlterarEMAIL):
        _translate = QtCore.QCoreApplication.translate
        AlterarEMAIL.setWindowTitle(_translate("AlterarEMAIL", "MainWindow"))
        self.label_2.setText(_translate("AlterarEMAIL", "CONFIRMAR  "))
        self.Remover.setText(_translate("AlterarEMAIL", "Alterar"))
        self.Remover_2.setText(_translate("AlterarEMAIL", "Cancelar"))
        self.label_3.setText(_translate("AlterarEMAIL", "ALTERAR EMAIL"))
        self.label.setText(_translate("AlterarEMAIL", "NOVO EMAIL "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AlterarEMAIL = QtWidgets.QMainWindow()
    ui = Ui_AlterarEMAIL()
    ui.setupUi(AlterarEMAIL)
    AlterarEMAIL.show()
    sys.exit(app.exec_())


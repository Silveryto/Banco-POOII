# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'depositar.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Depositar(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 288)
        Form.setStyleSheet("background-color: rgb(66, 132, 198)")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(250, 10, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(250, 180, 75, 23))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 150, 113, 16))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(160, 150, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 120, 113, 16))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(170, 120, 71, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_5.setObjectName("label_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 90, 113, 16))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(180, 90, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 220, 75, 23))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "Depositar"))
        self.pushButton.setText(_translate("Form", "Depositar"))
        self.label_3.setText(_translate("Form", "Deposito:"))
        self.label_5.setText(_translate("Form", "Senha:"))
        self.label_6.setText(_translate("Form", "Cpf:"))
        self.pushButton_2.setText(_translate("Form", "<<Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Tela_Depositar()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

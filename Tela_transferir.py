# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'transferir.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Tela_Transferir(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(554, 409)
        Form.setStyleSheet("background-color: rgb(66, 132, 198)\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 120, 251, 20))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(260, 290, 91, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 330, 91, 31))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255)")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(180, 80, 251, 20))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(50, 80, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(190, 160, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(100, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_10.setObjectName("label_10")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(100, 220, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255)")
        self.label_9.setObjectName("label_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(190, 250, 231, 20))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(190, 220, 231, 20))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 255, 255)")
        self.lineEdit_9.setObjectName("lineEdit_9")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Tranferir"))
        self.label_3.setText(_translate("Form", "Enviar:"))
        self.pushButton.setText(_translate("Form", "Enviar"))
        self.pushButton_2.setText(_translate("Form", "<<Voltar"))
        self.label_4.setText(_translate("Form", "CPF_destinatario:"))
        self.label_5.setText(_translate("Form", "Confirme_Seus_dados"))
        self.label_10.setText(_translate("Form", "Sua_senha:"))
        self.label_9.setText(_translate("Form", "Seu_CPF:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Tela_Transferir()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

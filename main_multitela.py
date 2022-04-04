import sys
import os
import mysql.connector

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from Tela_cadastro import Tela_Cadastro
from Tela_login import Tela_Login
from Tela_inicial import Tela_Inicial
from Tela_cliente import Tela_cliente
from Tela_depositar import Tela_Depositar
from Tela_sacar import Tela_Sacar
from Tela_transferir import Tela_Transferir


from classes import Pessoa
from classes import Cadastro
from classes import Cadastro_Bd

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        "função onde é feita a declaração das telas principais com seus respectivos stacks"
        Main.setObjectName('Main')
        Main.resize(640, 480)
        
        self.QtStack = QtWidgets.QStackedLayout()
        
        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        
        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)
        
        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)
        
        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack2)
        
        self.tela_cliente = Tela_cliente()
        self.tela_cliente.setupUi(self.stack3)
        
        self.tela_deposito = Tela_Depositar()
        self.tela_deposito.setupUi(self.stack4)
        
        self.tela_sacar =    Tela_Sacar()
        self.tela_sacar.setupUi(self.stack5)
        
        self.tela_transferir =  Tela_Transferir()
        self.tela_transferir.setupUi(self.stack6)
        
        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        
        
class Main(QMainWindow, Ui_Main):
    def __init__(self, parent = None):
        "aqui ocorre a ligação das telas com os botões funcionais e as chamadas das mesmas"
        super(Main, self).__init__(parent)
        self.setupUi(self)
        
        self.cad = Cadastro()
        self.cad1 = Cadastro_Bd()
        self.tela_inicial.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicial.pushButton_2.clicked.connect(self.abrirTelaLogin)
        self.tela_inicial.pushButton_3.clicked.connect(self.sair)

    
        self.tela_cadastro.pushButton_2.clicked.connect(self.botaoCadastra)
        self.tela_login.pushButton_2.clicked.connect(self.botaoLogin)
        self.tela_cadastro.pushButton.clicked.connect(self.voltar)
        self.tela_login.pushButton.clicked.connect(self.voltar)
        self.tela_cliente.pushButton_4.clicked.connect(self.voltar)
        self.tela_cliente.pushButton_2.clicked.connect(self.botaoDeposito)
        self.tela_deposito.pushButton.clicked.connect(self.depositar)
        self.tela_deposito.pushButton_2.clicked.connect(self.voltar_cliente)
        self.tela_cliente.pushButton.clicked.connect(self.botaoSacar)
        self.tela_sacar.pushButton.clicked.connect(self.sacar)
        self.tela_sacar.pushButton_2.clicked.connect(self.voltar_cliente)
        
        self.tela_cliente.pushButton_3.clicked.connect(self.botaoTranfere)
        self.tela_transferir.pushButton_2.clicked.connect(self.voltar_cliente)
        self.tela_transferir.pushButton.clicked.connect(self.Tranfere)
        
        
    def voltar(self):
        self.QtStack.setCurrentIndex(0)
    
    def voltar_cliente(self):
        self.QtStack.setCurrentIndex(3)
        
    def sair(self):
        exit()
    
    def botaoCadastra(self):
        "abaixo está todas as variaveis que sao usadas para fazer o preenchimento dos dados, e logo em seguidas conectados a uma linha"
        "e então realizada a passagem para as funções lá da parte de classes"
        nome = self.tela_cadastro.lineEdit.text()
        endereco = self.tela_cadastro.lineEdit_3.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        nascimento = self.tela_cadastro.lineEdit_4.text()
        senha = self.tela_cadastro.lineEdit_5.text()
        saldo = float(self.tela_cadastro.lineEdit_6.text())      
        if not(nome == '' or endereco == '' or cpf == '' or nascimento == '' or senha == ''):
            p = Pessoa(nome, endereco, cpf, nascimento, senha, saldo)
            self.cad1.cadastra_db(p)
            if(self.cad.cadastra(p)):
                    QMessageBox.information(None, 'POOII', 'Cadastro Realizado')
                    self.tela_cadastro.lineEdit.setText('')
                    self.tela_cadastro.lineEdit_2.setText('')
                    self.tela_cadastro.lineEdit_3.setText('')
                    self.tela_cadastro.lineEdit_4.setText('')
                    self.tela_cadastro.lineEdit_5.setText('')
                    self.tela_cadastro.lineEdit_6.setText('')
            else:
                QMessageBox.information(None, 'POOII', "Cpf ja cadastrado!!")
        else:
            QMessageBox.information(None, "POOII", 'Todos os valores precisam ser preenchidos')
        
    def botaoLogin(self):
        "realizado as condições para fazer o login, onde é passado o cpf e a senha"
        cpf = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        pessoa = self.cad.login(cpf, senha)
        if(pessoa != None):
            self.QtStack.setCurrentIndex(3)
            self.tela_cliente.lineEdit.setText(pessoa['nome'])
            self.tela_cliente.lineEdit_2.setText(pessoa['cpf'])
            sald = pessoa['saldo']
            self.tela_cliente.lineEdit_4.setText(str(sald))
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,"POOII", "Tente novamente!")
            self.tela_login.lineEdit.setText('')
            self.tela_login.lineEdit_2.setText('') 
            
            
    def botaoDeposito(self):
        "conexão para chamar a tela de deposito"
        self.QtStack.setCurrentIndex(4)
    
    def botaoTranfere(self):
        "conexão para chamar a tela de transderencia"
        self.QtStack.setCurrentIndex(6)
        
    def botaoSacar(self):
        "conexão para chamar a tela de saque"
        self.QtStack.setCurrentIndex(5)
    
    def depositar(self):
        "função para o deposito, onde passa a senha e o cpf e o valor, e entao é chamado para o metodo depositar"
        cpf = self.tela_deposito.lineEdit_4.text()
        senha = self.tela_deposito.lineEdit_3.text()
        deposito = self.tela_deposito.lineEdit_2.text()
        dep = self.cad.depositar(cpf, senha, deposito)
        if(dep == True):
            QMessageBox.information(None,"POOII", "Deposito Efetuado! efetue o login novamente!")
            self.tela_deposito.lineEdit_3.setText('')
            self.tela_deposito.lineEdit_4.setText('')
            self.tela_deposito.lineEdit_2.setText('')
            self.QtStack.setCurrentIndex(0)
        else:
            QMessageBox.information(None,"POOII", "Tente novamente!")
            self.tela_deposito.lineEdit_3.setText('')
            self.tela_deposito.lineEdit_4.setText('')
            self.tela_deposito.lineEdit_2.setText('')
            
    def sacar(self):
        "função para o saque, onde passa a senha e o cpf e o valor, e entao é chamado para o metodo sacar"
        cpf = self.tela_sacar.lineEdit_3.text()
        senha = self.tela_sacar.lineEdit_4.text()
        sacar = self.tela_sacar.lineEdit_2.text()
        saque = self.cad.sacar(cpf, senha, sacar)
        if(saque == True):
            QMessageBox.information(None,"POOII", "Saque Efetuado! Deslogue e logue novamente")
            self.tela_sacar.lineEdit_3.setText('')
            self.tela_sacar.lineEdit_4.setText('')
            self.tela_sacar.lineEdit_2.setText('')
        else:
            QMessageBox.information(None,"POOII", "Tente novamente!")
            self.tela_sacar.lineEdit_3.setText('')
            self.tela_sacar.lineEdit_4.setText('')
            self.tela_sacar.lineEdit_2.setText('')
            
    def Tranfere(self):
        "mesma coisa que os de cima, mas para transferencia"
        cpf_cliente = self.tela_transferir.lineEdit_9.text()
        cpf_destinatario = self.tela_transferir.lineEdit_3.text()
        valor = self.tela_transferir.lineEdit_2.text()
        senha = self.tela_transferir.lineEdit_8.text()
        enviar = self.cad.transferir(cpf_cliente, cpf_destinatario, valor, senha)
        if(enviar == True):
            QMessageBox.information(None,"POOII", "Transferencia Efetuada")
            self.tela_transferir.lineEdit_9.setText('')
            self.tela_transferir.lineEdit_3.setText('')
            self.tela_transferir.lineEdit_2.setText('')
            self.tela_transferir.lineEdit_8.setText('')   
        else:
            QMessageBox.information(None,"POOII", "Tente novamente!")
            self.tela_transferir.lineEdit_9.setText('')
            self.tela_transferir.lineEdit_3.setText('')
            self.tela_transferir.lineEdit_2.setText('')
            self.tela_transferir.lineEdit_8.setText('') 
                        
    def abrirTelaCadastro(self):
        "chama a tela de cadastro"
        self.QtStack.setCurrentIndex(1)
    
    def abrirTelaLogin(self):
        "chama a tela de login"
        self.QtStack.setCurrentIndex(2)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
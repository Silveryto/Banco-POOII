from tkinter.tix import Tree
from unittest import result
import mysql.connector

class Pessoa:
    __slots__ = ['_nome', '_endereco', '_cpf', '_nascimento', '_senha', '_saldo']
    
    def __init__(self, nome, endereco, cpf, nascimento, senha, saldo):
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento
        self._senha = senha
        self._saldo = saldo
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def endereco(self):
        return self._endereco
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nascimento(self):
        return self._nascimento
    
    @property
    def senha(self):
        return self._senha
    
    @property
    def saldo(self):
        return self._saldo
        
    @saldo.setter
    def saldo(self, saldo):
        return self._saldo
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
        

class Cadastro():

    def __init__(self):
        pass
    
    def cadastra(self, pessoa):
            conexao = mysql.connector.connect(host='localhost', database='banco', user='root', passwd='vinicius12')
            cursor = conexao.cursor()
            sql = """CREATE TABLE if NOT EXISTS usuarios_banco(cpf VARCHAR(11) PRIMARY KEY,
            nome text NOT NULL, senha VARCHAR(32) NOT NULL, endereco text NOT NULL, nascimento text NOT NULL, saldo float NOT NULL);"""
            cursor.execute(sql)
            try:
                cursor.execute('INSERT INTO usuarios_banco(cpf, nome, senha, endereco, nascimento, saldo) VALUES (%s, %s,%s, %s, %s, %s)', (pessoa.cpf, pessoa.nome, pessoa.senha, pessoa.endereco, pessoa.nascimento, pessoa.saldo))
                conexao.commit()
                conexao.close()
                return True
            except:
                conexao.commit()
                conexao.close()
                return False
                
    def login(self, cpf, senha):
        conexao = mysql.connector.connect(host='localhost', database='banco', user='root', passwd='vinicius12')
        cursor = conexao.cursor()
        sql = """CREATE TABLE if NOT EXISTS usuarios_banco(cpf VARCHAR(11) PRIMARY KEY,
        nome text NOT NULL, senha VARCHAR(32) NOT NULL, endereco text NOT NULL, nascimento text NOT NULL, saldo float NOT NULL);"""
        cursor.execute(sql)
        try:
            cpf_v = "SELECT * FROM usuarios_banco WHERE cpf ='{}'".format(cpf)
            cpf_senha = "SELECT * FROM usuarios_banco where senha ='{}'".format(senha)
            cursor.execute(cpf_v)
            resultado = cursor.fetchall()
            cursor.execute(cpf_senha)
            result = cursor.fetchall()
            
            if(len(resultado) != 0 and len(result) != 0):
                return resultado
            else:
                return False
        except:
            return False
    
    
    def deposito(self, cpf, senha, deposito):
        conexao = mysql.connector.connect(host='localhost', database='banco', user='root', passwd='vinicius12')
        cursor = conexao.cursor()
        sql = """CREATE TABLE if NOT EXISTS usuarios_banco(cpf VARCHAR(11) PRIMARY KEY,
        nome text NOT NULL, senha VARCHAR(32) NOT NULL, endereco text NOT NULL, nascimento text NOT NULL, saldo float NOT NULL);"""
        cursor.execute(sql)
        login = Cadastro.login(self, cpf, senha) 
        
        if(login != None):
            d = (float(deposito) + float(login[0][5]))
            l = login[0][0]
            cursor.execute("UPDATE usuarios_banco  SET saldo = %s WHERE cpf = %s ", (d, l))
            conexao.commit()
            conexao.close()
            return True
        else:
            print("Deposito nao efetuado")
            return False
            
    
    def sacar(self, cpf,senha, sacar):
        conexao = mysql.connector.connect(host='localhost', database='banco', user='root', passwd='vinicius12')
        cursor = conexao.cursor()
        retorno = Cadastro.login(self, cpf, senha)
        
        if retorno != False:
            if float(retorno[0][5]) >=  float(sacar):
                d = (float(retorno[0][5]) - float(sacar))
                l = retorno[0][0]
                cursor.execute('UPDATE usuarios_banco SET saldo = %s WHERE cpf = %s', (d, l))
                conexao.commit()
                conexao.close()
                return True
            else:
                return False
        else:
            return False

    def transferir(self, cpf, cpf_d, valor, senha):
        retorno = Cadastro.login(self, cpf, senha)
        conexao = mysql.connector.connect(host='localhost', database='banco', user='root', passwd='vinicius12')
        cursor = conexao.cursor()
        valor1 = float(retorno[0][5])
        if (valor <= valor1): 
            Cadastro.sacar(self, cpf, senha, valor)
            cpf_iv = "SELECT * FROM usuarios_banco WHERE cpf = '{}'".format(cpf_d)
            cursor.execute(cpf_iv)
            result = cursor.fetchall()
            f = (float(result[0][5]) + float(valor))
            cursor.execute('UPDATE usuarios_banco SET saldo = %s WHERE cpf = %s', (f, cpf_d))
            conexao.commit()
            conexao.close()
            return True
        else:
            return False


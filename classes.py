import mysql.connector

class Pessoa:
    __slots__ = ['_nome', '_endereco', '_cpf', '_nascimento', '_senha', '_saldo']
    
    def __init__(self, nome, endereco, cpf, nascimento, senha, saldo):
        "metodo onde é feito o armazenamento dos dados inseridos quando criado uma classe do tipo pessoa"
        self._nome = nome
        self._endereco = endereco
        self._cpf = cpf
        self._nascimento = nascimento
        self._senha = senha
        self._saldo = saldo

    @property
    def nome(self):
        "metodo onde retorna o proprio nome"
        return self._nome
    
    @property
    def endereco(self):
        "metodo onde retorna o proprio endereço"
        return self._endereco
    
    @property
    def cpf(self):
        "metodo onde retorna o proprio cpf"
        return self._cpf
    
    @property
    def nascimento(self):
        "metodo onde retorna o proprio nascimento"
        return self._nascimento
    
    @property
    def senha(self):
        "metodo onde retorna o proprio senha"
        return self._senha
    
    @property
    def saldo(self):
        "metodo onde retorna o proprio saldo"
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
        

class Cadastro_Bd:

    def __init__(self) -> None:
        pass

    def cadastra_db(self, pessoa):
        "metodo onde é feito o armazenamento dos dados inseridos quando criado uma classe do tipo pessoa"
        conexao = mysql.connector.connect(host='localhost', database='banco', user='root', passwd='V1nicius')
        cursor = conexao.cursor()

        nome = pessoa.nome
        senha = pessoa.senha
        endereco = pessoa.endereco
        nascimento = pessoa.nascimento
        cpf = pessoa.cpf
        saldo = pessoa.saldo

        sql = f"""CREATE TABLE IF NOT EXISTS usuarios_banco(cpf VARCHAR(11) PRIMARY KEY,
        nome text NOT NULL, senha VARCHAR(32) NOT NULL, endereco text NOT NULL, nascimento DATE NOT NULL, saldo integer NOT NULL);"""

        
        cursor.execute(sql)
        cursor.execute('INSERT INTO usuarios_banco(cpf, nome, senha, endereco, nascimento, saldo) VALUES (%s, %s,MD5(%s), %s, %s, %s)', (cpf, nome, senha, endereco, nascimento, saldo))
        conexao.commit()
        conexao.close()

class Cadastro:
    __slots__ = ['_lista']
    
    def __init__(self):
        "metodo que inicia uma lista de cadastro dentro da classe cadastro"
        self._lista = []
    
    def cadastra(self, pessoa):
        "metodo onde insere um cadastro ja realizado com a classe pessoa na lista de cadastro, realizando assim um cadastro"
        existe = self.busca(pessoa.cpf)
        if(existe == None):
            p = {'nome': pessoa.nome, 'endereco': pessoa.endereco, 'cpf': pessoa.cpf, 
                 'nascimento': pessoa.nascimento, 'senha': pessoa.senha, 'saldo': pessoa.saldo}
            self._lista.append(p)
            return True
        else:
            return False
    
    def busca(self, cpf):
        "metodo para fazer a buscar e verificar se já existe um cpf"
        for lp in self._lista:
            if lp['cpf'] == cpf:
                return lp
        return None 
        
    def login(self, cpf, senha):
        "metodo que verifica o login"
        for pessoa in self._lista:
            if pessoa['cpf'] == cpf and pessoa['senha'] == senha:
                return pessoa
        return None
        
    def sacar(self, cpf,senha, sacar):
        "metodo usado para sacar onde verifica se o saldo é suficiente e então realizar o saque"
        for pessoa in self._lista:
            if pessoa['cpf'] == cpf and pessoa['senha'] == senha:
                if pessoa['saldo'] >= float(sacar):
                    pessoa['saldo'] -= float(sacar)
                    return True
        return False
    
    def depositar(self, cpf, senha, deposito):
        "metodo para realizar um deposito"
        for pessoa in self._lista:
            if pessoa['cpf'] == cpf and pessoa['senha'] == senha:
                pessoa['saldo'] += float(deposito)
                return True
        return False
        
    def transferir(self, cpf, cpf_d, valor, senha):
        "metodo para realizar uma transferencia"
        for pessoa in self._lista:
            if pessoa['cpf'] == cpf and pessoa['senha'] == senha and pessoa['saldo'] >= float(valor):
                for i in self._lista:
                    if i['cpf'] == cpf_d:
                        i['saldo'] += float(valor)
                        pessoa['saldo'] -= float(valor)
                        return True
        return False
      



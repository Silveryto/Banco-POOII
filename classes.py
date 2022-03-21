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
        

class Cadastro:
    __slots__ = ['_lista']
    
    def __init__(self):
        self._lista = []
    
    def cadastra(self, pessoa):
        existe = self.busca(pessoa.cpf)
        if(existe == None):
            p = {'nome': pessoa.nome, 'endereco': pessoa.endereco, 'cpf': pessoa.cpf, 
                 'nascimento': pessoa.nascimento, 'senha': pessoa.senha, 'saldo': pessoa.saldo}
            self._lista.append(p)
            print(self._lista)
            return True
        else:
            return False
    
    def busca(self, cpf):
        for lp in self._lista:
            if lp['cpf'] == cpf:
                return lp
        return None 
        
    def login(self, cpf, senha):
        for pessoa in self._lista:
            if pessoa['cpf'] == cpf and pessoa['senha'] == senha:
                return pessoa
        return None
        
    def sacar(self, cpf,senha, sacar):
       for pessoa in self._lista:
            if pessoa['cpf'] == cpf and pessoa['senha'] == senha:
                if pessoa['saldo'] >= float(sacar):
                    pessoa['saldo'] -= float(sacar)
                    return True
       return False
    
    def depositar(self, cpf, senha, deposito):
        for pessoa in self._lista:
            if pessoa['cpf'] == cpf and pessoa['senha'] == senha:
                pessoa['saldo'] += float(deposito)
                return True
        return False
        
    def transferir(self, cpf):
        
        pass



class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Cliente(Pessoa): #Herança DE PESSOA
    pass

class Aluno(Pessoa):
    pass
    
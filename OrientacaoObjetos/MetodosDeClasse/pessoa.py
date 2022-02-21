from datetime import datetime
from random import randint

class Pessoa:
    ano_atual = datetime.now().year
   
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    
    
    def falar(self):
        print('Olá, meu nome é {} e tenho {} anos.'.format(self.nome, self.idade))
    
    def get_ano_nascimento(self):
         print('Data de Nascimento '  + str(self.ano_atual - self.idade))
    
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento #criando variavel dentro do escopo da classe
        return cls(nome,idade)

    @staticmethod
    def gera_id():
        rand = randint(0, 9999)
        return rand

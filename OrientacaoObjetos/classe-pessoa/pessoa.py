class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    
    
    def falar(self):
        print('Olá, meu nome é {} e tenho {} anos.'.format(self.nome, self.idade))
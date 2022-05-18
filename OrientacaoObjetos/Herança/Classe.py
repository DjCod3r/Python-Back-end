class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclass = self.__class__.__name__
    
    def falar(self):
        print(f'{self.nomeclass} está falando')


class Cliente(Pessoa): #Herança DE PESSOA
    def comprar(self):
        print(f'{self.nomeclass} está comprando')

    def falar(self):
        
        print(f'falando em Cliente')

class Aluno(Pessoa):
  def estudar(self):
    print(f'{self.nomeclass} está estudando')

class ClienteVIP(Cliente):
    def __init__(self,nome,idade,sobrenome):
        Pessoa.__init__(self,nome,idade)
        self.sobrenome = sobrenome
    def falar(self):
        print(f'{self.nome} {self.sobrenome} está falando')
#Composicao
class Cliente:
    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade
        self.endereco = [] #depende da Class add_endereco
    
    

    def add_endereco(self, cidade, estado): #para adicionar um endereço depende da Class Endereco
        self.endereco.append(Endereco(cidade, estado))
    
    def mostra_endereco(self):
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)

class Endereco:
    def __init__(self,estado, cidade):
        self.estado = estado
        self.cidade = cidade
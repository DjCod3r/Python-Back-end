class Produto:
    def __init__(self, nome ,preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, porcentagem):
        self.preco = self.preco - (self.preco * porcentagem / 100)

    #Getter
    @property
    def preco(self): #pega o preço e retorna _preco
        return self._preco
    
    #Setter
    @preco.setter
    def preco(self, valor): #Se valor for string mudar para float e alterar valores
        if isinstance(valor, str): #Se for string
            valor = float(valor.replace('R$','').replace('.','').replace(',','.')) #Replace R$ e virgula por ponto
        self._preco = valor #Atribuindo valor a variavel









p1 = Produto('Camisa', 'R$20,00')
p1.desconto(10)
print(p1.preco)
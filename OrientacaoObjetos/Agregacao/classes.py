

class Carrinho_Compra:
    def __init__(self):
        self.itens = []

    def adiciona(self, item):
        self.itens.append(item)

    def mostra(self):
        for item in self.itens:
            print(item.nome, item.preco)
    
    def total(self):
        total = 0
        for item in self.itens:
            total += item.preco
        return total
   


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    
from classes import Produto, Carrinho_Compra


camisa = Produto('Camiseta', 50)
calca = Produto('Tenis', 40)

carrinho = Carrinho_Compra()
carrinho.adiciona(camisa)
carrinho.adiciona(calca)
carrinho.mostra()
print(carrinho.total())
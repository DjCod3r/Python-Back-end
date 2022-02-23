from classEndereco import Endereco , Cliente

cliente1 = Cliente('Joao', 25)
cliente1.add_endereco('Sao Paulo', 'SP')

cliente2 = Cliente('Maria', 20)
cliente2.add_endereco('Rio de Janeiro', 'RJ')

print(cliente1.nome)
cliente1.mostra_endereco()
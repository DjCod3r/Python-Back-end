from Dados import pessoas, produtos, lista


novaLista = filter(lambda valor: valor > 5, lista)
for valor in novaLista:
    print(valor)


produtosRetornaMaior = filter(lambda p: p['preco'] > 8, produtos)
for p in produtosRetornaMaior:
    print(p)


produtosRetornaNome = filter(lambda p: p['nome'] == 'Caneta', produtos)
for p in produtosRetornaNome:
    print(p)



# filter padrão
produtoPreco = filter(lambda x: x > 5, lista)
print(list(produtoPreco))


# utilizando list comprehension
listaNova = [x for x in lista if x > 5]
print(listaNova)


print()
print('Pessoas Maior de Idade:')
filtroPessoasIdade = filter(lambda i: i['idade'] > 18, pessoas)
for pessoa in filtroPessoasIdade:
    print(pessoa)
print()
print('Pessoas Manor de Idade:')
filtroPessoasMenorIdade = filter(lambda i: i['idade'] < 18, pessoas)
for pessoa in filtroPessoasMenorIdade:
    print(pessoa)

print()
#Filtrando os produtos

print('Produtos com preço maior que 8:')
filtroProdutos = filter(lambda p:p['preco'] > 8, produtos)
for p in filtroProdutos:
    print(p)

print()
print('Produtos com preço menor que 8:')
filtroProdutosMenorPreco = filter(lambda p:p['preco'] <= 8 , produtos)
for p in filtroProdutosMenorPreco:
    print(p)
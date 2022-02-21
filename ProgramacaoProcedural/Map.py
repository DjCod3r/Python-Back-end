from Dados import pessoas, produtos, lista



#novaLista = map(lambda x: x*2, lista)
#novaLista = [x * 2 for x in lista]
#print(list(novaLista))


precos = map(lambda p: p['preco'], produtos ) 
for preco in precos:
    print(preco)
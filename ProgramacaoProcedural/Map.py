from Dados import pessoas, produtos, lista



#novaLista = map(lambda x: x*2, lista)
#novaLista = [x * 2 for x in lista]
#print(list(novaLista))


for p in produtos:
    print(p)
print()
print("#####################################")
print()
print("Produtos com precos aumentados:")
print()

def aumento(p):
    p['preco'] = round(p['preco'] * 1.1, 2)
    return p


Novosprecos = map(aumento, produtos ) 
for preco in Novosprecos:
    print(preco)





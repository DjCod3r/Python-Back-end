#Split
string = "Teste de split dividindo por espaço"
lista = string.split(' ')
print(lista)

for valor in lista:
    print(valor)
juntarLista = ' '.join(lista) #juntando lista
print(juntarLista)


for indice , valor in enumerate(lista): 
    print(indice , valor)
import sys
lista = list(range(1, 10000000))


print(sys.getsizeof(lista)) #consumo de memoria
print(sys.getwindowsversion()) 
print(sys.platform)
print(sys.version)


def geraLista():
    lista = []
    for x in range(100):
        lista.append(x)
    return lista
print(geraLista())

#criando generator

def geraLista2():
    for x in range(100):
        yield x
    return lista
gera = geraLista2()
print(gera)
for valor in gera:
    print(valor)


lista2 = [x for x in range(100)]
print(type(lista2))
lista3 = (x for x in range(100))
print(type(lista3))

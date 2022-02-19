from sympy import li


a = lambda x , y : x * y
print(a(2,3))
b = lambda x , y : x + y
print(b(2,3))
c = lambda x , y : x / y
print(c(2,3))
d = lambda x , y : x - y
print(d(2,3))


lista = [
    ['P1' , 20],
    ['P2' , 5],
    ['P3' , 10],
]

listaOrdenadaLambda = lambda lista : sorted(lista, key=func) #utilizando lambda

def func(item):
    return item[1] # retorna o valor da segunda posicao da lista

lista.sort(key=func , reverse=True) # Ordena a lista de forma decrescente
lista.sort(key=lambda item: item[1], reverse=True) # Ordena a lista de forma decrescente
print(lista)

print(sorted(lista, key=lambda x: x[1])) # Ordena a lista de forma decrescentes


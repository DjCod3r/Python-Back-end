set1 = {1 , 2, 3, 4, 5} #set suporta elementos imutaveis
print(set1)



for x in set1:
    print(x)


set1.add(6 )
print(set1)
set1.discard(5)
print(set1)

set1.update('Python')
print(set1)


#set ordena os elementos numericos
set2 = {2 , 3, 5, 4}
print(set2)

x = {3 , 5 , 8}
y = {2 , 3 , 5 , 7}
z = x.union(y) #uniao de conjuntos
print(f'valor de z {z}')

w = x.intersection(y) #intersecao de conjuntos , elementos que estão presentes nos 2 conjuntos
print(f'valor de w {w}')

a = x.difference(y) # elementos que existem apenas no conjunto x
print(f'valor de a {a}')

b = x.symmetric_difference(y) # elementos unicos no conjunto x ou y
print(f'valor de b {b}')
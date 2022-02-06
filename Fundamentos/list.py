l1 = [1 , 2, 3]
l2 = [4 , 5, 6]
print(l1 , l2)
l2.insert(0, 4) #inserir no indice 0 o valor 4
l2.append(5) #adicionar valor ao final
l3 = l1 + l2 #concatenar
l1.extend(l2) #concatenar

print(l3)
print(l1)

l4 = [ 5 , 6, 7, 8, 9]

del(l4[:2])
print(l4)
l4.pop() #remover ultimo
print(l4)

l5= list(range(1,10)) #transformar em iteravel com list
print( l5)
m = ''
for v in l5:
    m += str(v)
print(m)

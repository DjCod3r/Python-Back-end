listC1 = [1, 2, 3, 4, 5]
listC2 = [6, 7, 8, 9, 10]



receptor = [x for x in listC1 if x > 3]
print(receptor)
print([x for x in listC1])
print([x for x in listC1])




a = [(x, y) for x in listC1 for y in range(2)]

print("Este e o valor" + str([valor ** 2 for valor in listC1]))
print(a)


l5 = ['Djonatan', 'Schvambach', 'Python', 'Java', 'C++']

print([ valor.replace('a', '@') for valor in l5])



#utilizar com Dictionary
dictD1 = {'nome': 'Djonatan', 'sobrenome': 'Schvambach', 'idade': 25, 'altura': 1.76, 'peso': 58}

print({x: y for x, y in dictD1.items()})




from itertools import combinations
from itertools import permutations

nome = ['Djonatan' , 'Lucas' , 'Cris' , 'Julia' , 'Pedro']

for elemento in combinations(nome, 2):
    print(elemento)



for grupo in permutations(nome, 2):
    print(grupo)


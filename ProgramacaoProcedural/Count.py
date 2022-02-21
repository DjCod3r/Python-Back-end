#count retorna o valor de uma lista
from itertools import count

v = count(1)
for i in v:
    print(i)
    if i == 15:
        break
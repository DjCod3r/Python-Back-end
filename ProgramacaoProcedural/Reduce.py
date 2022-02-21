from functools import reduce
from Dados import pessoas, produtos, lista


somaLista = reduce(lambda ac, y: ac + y, lista)
print(somaLista)

somaPreco = reduce(lambda ac, y: ac + y['preco'], produtos, 2)
print(round(somaPreco, 2))

somaIdade = reduce(lambda ac, y: ac + y['idade'], pessoas, 0)
print(somaIdade)
from itertools import groupby

from sympy import ordered

#lista de alunos
alunos = [
    {'nome': 'Maria', 'nota': 'A'},
    {'nome': 'João', 'nota': 'B'},
    {'nome': 'Pedro', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'Paulo', 'nota': 'B'},
    {'nome': 'Rafael', 'nota': 'A'},
    {'nome': 'Ana', 'nota': 'C'},
    {'nome': 'Paulo', 'nota': 'B'},
    {'nome': 'Rafael', 'nota': 'A'},

]

#funcão que ordena a lista de alunos
ordena = lambda aluno: aluno['nota']

#ordenar
alunos.sort(key=ordena)

#agrupar os alunos por nota
groupByNote = groupby(alunos, ordena)

#imprimir os alunos por nota
for agrupamento , valoresAgrupados in groupByNote:
    print(f'Alunos Com nota {agrupamento}' )
    for aluno in valoresAgrupados:
        print(aluno.get('nome'))
    print()
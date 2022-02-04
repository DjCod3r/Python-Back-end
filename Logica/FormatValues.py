#Formatar valores
# :s para String
# :f valores flutuantes
# :d valores inteiros

a = 10
b = 32
solucao = a / b
print('{:.2f}'.format(solucao)) #formatar 2 casas decimais
print(f'{solucao:.2f}') #formatar 2 casas decimais

#colocar numeros a direita
print(f'{a:0<5}')
print(f'{b:0<5}')

#colocar numeros no centro , preenchimentos com 0
print(f'{a:0^10}')
print(f'{b:0^10}')

nome = 'Djonatan'
print(f'{nome:#^10}')
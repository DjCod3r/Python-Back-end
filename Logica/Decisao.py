a = 15
b = 15
exp = a == b
if a < b:
    print(f'{a} e menor que {b}')
elif a > b :
    print(f'{a} e maior que {b}')
else:
    print('Os valores são iguais')

letra = 'l'
nome = 'Djonatan l'
if letra in nome:
    print(f'Contem {letra} no nome')
else:
    print(f'Não Contem {letra} no nome')

valor = '2'
valores = '82718939289172'
if valor in valores:
    print(f'Contem o valor {valor} em {valores}')

i = 0
for valor in valores:
    if valor in valores[i]:
        i += 1
    print(i)






#idade = int(input("Sua idade? "))
#if idade < 20 or idade > 30:
 #   print('Você não pode pegar emprestimos')
#else:
#    print('Voce pode pegar emprestimos')

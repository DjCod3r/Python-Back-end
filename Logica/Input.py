nome = input('Qual seu nome ? ')

print(f'Nome do usuario {nome} \n'
      f'Tipo do dado {type(nome)}')

idade = int(input('Qual sua idade? '))

print(f'Idade do usuario {idade} \n'
      f'Tipo de dado {type(idade)}')

altura = float(input('Qual sua altura? '))

print(f'A altura do usuario e {altura}\n'
      f'O tipo de dado é {type(altura)}')

anoNascimento = 2022 - idade
print('O ano de Nascimento do usuario e ' + str(anoNascimento))

num1 = int(input('Digite o primeiro numero da soma '))
num2 = int(input('Digite o segundo numero da soma '))
print(num1 + num2)


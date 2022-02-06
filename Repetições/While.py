'''nome = ''
while nome != 'Djon':
    nome = input('Qual seu nome?')
    print(f'ola {nome}')
print('Acertou o nome')'''
x = 0

while x < 10:
    j = 0
    while j <= 9:
        k = 0
        while k <= 9:
            print(f'{x}{j}{k}')
            k += 1
        j += 1
    x += 1

frase = 'teste de iteracao com while'
tamanho = len(frase)
contagem = 0
string = ''
while contagem < tamanho:
    print(string)
    print(contagem, frase[contagem])
    string += frase[contagem]
    contagem += 1
print(string)







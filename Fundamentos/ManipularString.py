texto = 'Djonatan'
print(texto[2])

print(texto[-1])
#buscar do 0 ao 4
novoTxt = texto[0:4]
print(novoTxt)

#buscar do 0 ao 7 pulando de 0 em 2
novoTxt = texto[0:7:2]
print(novoTxt)
#printar indice 2 e 3
print(texto[2:4])

#verificação simples
a = 'Djon'
if a in texto:
    print(a)
#string inteira
print(texto[0:])
print(len(texto))
for letra in texto:
    print(letra)
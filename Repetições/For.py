
text = 'texto'

for letra in text:
    print(letra)

for n in range(10):
    print(n)

for n in range(0 , 11 , 2): #inicio , fim , step
    print(n)

for n in range(100):
    if n % 5 == 0:
        print(n)

texto = 'python'
novastring = ''
for letra in texto:
    if letra == 'p':
        novastring += letra.upper()
    else:
        novastring += letra
print(novastring)
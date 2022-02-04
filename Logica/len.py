nome = input("Digite seu nome ")
valorc = len(nome)
print(f"o nome {nome} contem {valorc} caracteres e o tipo do dado é {type(nome)}")

if valorc < 2:
    print('O Nome deve conter mais de 2 caracteres')
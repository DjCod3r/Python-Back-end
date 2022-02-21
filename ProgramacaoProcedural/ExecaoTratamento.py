

try:
    print(a)
except NameError as e:
    print('Não existe variável a' ,e)


def dividir(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as e:
        print('Não é possível dividir por zero', e)
        raise #captura a execao e re-lança

try: #tratando aqui e não no bloco try acima
    print(dividir(5, 0))
except Exception as e:
    print('Erro:', e)


n = int(input('Digite um número: '))

print(n + 5)

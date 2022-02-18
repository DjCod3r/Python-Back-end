

from ast import arg


def retornaCubo(value):
    return value ** 3

print(retornaCubo(5))

def div (n1, n2):
    return n1 / n2
print(div(10 , 2))

def func(*args):
    print(len(args))
    for i in args:
        print(i)
    return sum(args)    # quando n sabemos quantos args vamos receber


print(func(1,2,3,4,5,6,7,8,9,10))


lista = [1  ,2 ,3 , 4 ,5 ,6 ,7 ,8 ,9 ,10]
n1 , n2 , *n = lista
print(n1, n2, n)

valor = 'a'
def fun(value):
    print(valor)

def funcao(value):
    global valor
    valor = 'b'
    print(valor)
fun(valor)

fun(valor)
funcao(valor)




variavel = 'valor'

def func():
    print(variavel)



def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
outra = func2(arg=variavel)
print(outra)

#def funcFala():
#    print("Fala")


#falar = funcFala
#falar()


def master(funcao):
    def slave():
        print("Decorada")
        funcao()
    return slave

@master
def funcOi():
    print("Oi")
    


funcOi()
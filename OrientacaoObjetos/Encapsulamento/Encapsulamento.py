class Basededados:
    def __init__(self):
        self._dados = {}


    def inserir_cliente(self,id , nome):
        if 'clientes' not in self._dados: #Se o cliente não existir nos dados
            self._dados['clientes'] = {id:nome} #o ID vai ser o nome
        else:
            self._dados['clientes'].update({id:nome}) #se já existir, atualiza o nome

    def lista_cliente(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)


    def apaga_cliente(self,id): #remover um cliente
        if 'clientes' in self._dados:
            if id in self._dados['clientes']:
                del self._dados['clientes'][id]


bd = Basededados()
bd.inserir_cliente(1, 'Joao')
bd.inserir_cliente(2, 'Maria')
bd.inserir_cliente(3, 'Pedro')



bd.apaga_cliente(2)
print(bd._dados)


bd.lista_cliente()
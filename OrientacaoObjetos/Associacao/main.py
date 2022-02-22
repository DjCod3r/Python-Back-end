from classes import Caneta, Escritor

escritor = Escritor('Lucas')
caneta = Caneta('Bic')



print(escritor.nome)
caneta.escrever()


escritor.ferramenta = caneta

escritor.ferramenta.escrever()
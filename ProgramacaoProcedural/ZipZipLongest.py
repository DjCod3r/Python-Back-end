from itertools import zip_longest
#criar lista com cidades
cidades = ['São leopoldo', 'Porto Alegre', 'Florianopolis' , 'São Paulo']


estados = ['RS', 'RS', 'SC', 'SP']

cidades_estados = zip(cidades, estados)
print(dict(cidades_estados))

#for cidade in cidades_estados:
    #print(cidade)





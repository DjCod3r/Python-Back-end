from pessoa import Pessoa

p1 = Pessoa('João', 20)
p2 = Pessoa('Maria', 25)

p1.falar()
p2.falar()

#p1.get_ano_nascimento()
#p2.get_ano_nascimento()

p4 = Pessoa.por_ano_nascimento('Pedro', 1990)
p4.get_ano_nascimento()
print(p4.idade)
print(p4.gera_id())

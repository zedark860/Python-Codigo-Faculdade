arquivo = open('dados.txt', 'r')

conteudo = arquivo.read()

print("Tipo de conteudo: ", type(conteudo))
print("Conteudo: ", repr(conteudo))

arquivo.close()

arquivo = open('dados.txt', 'r')

conteudo = arquivo.readline()

print("Conteúdo retornado pelo readline:")
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print("Proximo conteúdo retornado pelo readline:")
print(repr(proximo_conteudo))

arquivo.close()

arquivo = open('dados.txt', 'r')

conteudo = arquivo.readlines()

print("Conteúdo retornado pelo readlines:")
print(repr(conteudo))

arquivo.close()

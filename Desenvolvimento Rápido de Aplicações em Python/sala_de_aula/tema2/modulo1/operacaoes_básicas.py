import os

arquivo1 = open('dados.txt', 'r')
arquivo2 = open('/mnt/sdb1/Codes/Python-Codigo-Faculdade/Desenvolvimento Rápido de Aplicações em Python/sala_de_aula/dados.txt', 'r')

arquivo3 = open('documentos/dados2.txt', 'r')
arquivo4 = open('/mnt/sdb1/Codes/Python-Codigo-Faculdade/Desenvolvimento Rápido de Aplicações em Python/sala_de_aula/documentos/dados2.txt', 'r')

print(os.path.realpath(arquivo1.name))

print(os.path.abspath(arquivo2.name))

print(arquivo1)

# r : Abre o arquivo para leitura (default)
# w : Abre o arquivo para escrita, truncando o arquivo primeiro.
# x : Cria um arquivo para escrita e falha, caso ele exista.
# a : Abre o arquivo para escrita, acrescentando conteúdo ao final do arquivo, caso ele exista.
# b : Modo binário.
# t : Modo texto (default).
# + : Modo de leitura e escrita.


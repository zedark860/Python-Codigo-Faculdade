import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Pessoa
from script19_4 import recuperar_veiculos

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()

    comando: str = '''
        SELECT * FROM PESSOA
    '''
    cursor.execute(comando)
    
    pessoas: list[Pessoa] = []
    reg_pessoas: list[tuple] = cursor.fetchall()
    for reg_pessoa in reg_pessoas:
        pessoa: Pessoa = Pessoa(*reg_pessoa)
        pessoa.veiculos = recuperar_veiculos(conexao, pessoa.cpf)
        pessoas.append(pessoa)
        
    for pessoa in pessoas:
        print(pessoa.nome)
        for veiculo in pessoa.veiculos:
            print("\t", veiculo.placa, veiculo.marca.nome)
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

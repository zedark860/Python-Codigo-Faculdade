import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Pessoa

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()

    comando: str = '''
        SELECT * FROM PESSOA WHERE oculos=:usa_oculos
    '''
    cursor.execute(comando, {"usa_oculos": True})
    
    registros = cursor.fetchall()
    for registro in registros:
        pessoa: Pessoa = Pessoa(*registro)
        print("cpf:", type(pessoa.cpf), pessoa.cpf)
        print("nome:", type(pessoa.nome), pessoa.nome)
        print("nascimento", type(pessoa.data_nascimento), pessoa.data_nascimento)
        print("oculos:", type(pessoa.usa_oculos), pessoa.usa_oculos)
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

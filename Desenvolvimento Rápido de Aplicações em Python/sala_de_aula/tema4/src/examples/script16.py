import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()

    comando: str = '''
        SELECT nome, oculos FROM PESSOA 
    '''
    cursor.execute(comando)
    
    registros = cursor.fetchall()
    print("Tipo retornado pelo fetchall:", type(registros))

    for registro in registros:
        print("Tipo:", type(registro), "- Conteúdo:", registro)

except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    
    # Habilita as chaves estrangeiras, pois o sqlite3 não suporta isso por padrão
    conexao.execute("PRAGMA foreign_keys = on")
    cursor: Cursor = conexao.cursor()

    comando: str = '''
        DELETE FROM PESSOA
        WHERE cpf = 12345678900
    '''

    conexao.execute(comando)

    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

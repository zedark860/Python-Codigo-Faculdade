import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    
    # Habilita as chaves estrangeiras, pois o sqlite3 não suporta isso por padrão
    conexao.execute("PRAGMA foreign_keys = on")
    cursor: Cursor = conexao.cursor()

    comando1: str = '''
        UPDATE PESSOA
        SET oculos = 1
    '''
    conexao.execute(comando1)

    comando2: str = '''
        UPDATE PESSOA
        SET oculos = ?
        WHERE cpf = ?
    '''
    conexao.execute(comando2, (False, 30000000099))
    
    comando3: str = '''
        UPDATE PESSOA
        SET oculos = :usa_oculos
        WHERE cpf = :cpf
    '''
    conexao.execute(comando3, {"usa_oculos": False, "cpf": 20000000099})

    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

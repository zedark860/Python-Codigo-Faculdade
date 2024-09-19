import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()
    
    comando: str = """
        INSERT INTO PESSOA (cpf, nome, nascimento, oculos)
        VALUES (?, ?, ?, ?)
    """
    
    cursor.execute(comando, (12345678900, "João", "2000-01-31", True))
    
    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()
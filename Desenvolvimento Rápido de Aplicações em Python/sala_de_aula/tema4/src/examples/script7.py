import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()
    
    comando: str = """
        ALTER TABLE VEICULO 
        ADD COLUMN motor REAL
    """
    
    cursor.execute(comando)
    
    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()
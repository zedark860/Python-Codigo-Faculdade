import sqlite3
from sqlite3 import Connection, Cursor, DatabaseError

try:
    conexao: Connection = sqlite3.connect("../database/meu_banco.db")
    cursor: Cursor = conexao.cursor()
    
    comando: str = """
        CREATE TABLE PESSOA (
            cpf INTEGER NOT NULL,
            nome TEXT NOT NULL,
            nascimento DATE NOT NULL,
            oculos BOOLEAN NOT NULL,
            PRIMARY KEY (cpf)
        )
    """
    
    cursor.execute(comando)
    
    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()
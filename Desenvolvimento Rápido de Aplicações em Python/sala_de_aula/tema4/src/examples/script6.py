import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()
    
    comando: str = """
        CREATE TABLE VEICULO (
            placa CHARACTER(7) NOT NULL,
            ano INTEGER NOT NULL,
            cor TEXT NOT NULL,
            proprietario INTEGER NOT NULL,
            marca INTEGER NOT NULL,
            PRIMARY KEY (placa),
            FOREIGN KEY (proprietario) REFERENCES PESSOA(cpf),
            FOREIGN KEY (marca) REFERENCES MARCA(id)
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
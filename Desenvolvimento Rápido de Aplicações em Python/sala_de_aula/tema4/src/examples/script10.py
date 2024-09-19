import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Pessoa

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()
    
    pessoa: Pessoa = Pessoa(10000000099, "Maria", "1990-01-31", False)
    
    comando: str = """
        INSERT INTO PESSOA (cpf, nome, nascimento, oculos)
        VALUES (?, ?, ?, ?)
    """
    
    cursor.execute(comando, (pessoa.cpf, pessoa.nome, pessoa.data_nascimento, pessoa.usa_oculos))
    
    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()
import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Pessoa

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()
    
    pessoa: Pessoa = Pessoa(30000000099, 'Silva', '1990-03-30', True)
    
    comando: str = """
        INSERT INTO PESSOA (cpf, nome, nascimento, oculos)
        VALUES (:cpf, :nome, :data_nascimento, :usa_oculos)
    """
    
    # função vars retorna todos os atributos de um objeto na forma de dicionário
    cursor.execute(comando, vars(pessoa))
    print(vars(pessoa))
    
    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()
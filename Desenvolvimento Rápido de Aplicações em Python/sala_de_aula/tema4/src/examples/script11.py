import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Pessoa

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()
    
    pessoa: Pessoa = Pessoa(20000000099, 'José', '1990-02-28', True)
    
    comando: str = """
        INSERT INTO PESSOA (cpf, nome, nascimento, oculos)
        VALUES (:cpf, :nome, :data_nascimento, :usa_oculos)
    """
    
    cursor.execute(comando, {
        "cpf": pessoa.cpf,
        "nome": pessoa.nome,
        "data_nascimento": pessoa.data_nascimento,
        "usa_oculos": pessoa.usa_oculos
    })
    
    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()
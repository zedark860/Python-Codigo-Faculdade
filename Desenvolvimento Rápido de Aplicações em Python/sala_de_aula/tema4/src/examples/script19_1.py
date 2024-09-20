import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Veiculo

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()

    comando: str = '''
        SELECT * FROM VEICULO
    '''
    cursor.execute(comando)
    
    registros = cursor.fetchall()
    for registro in registros:
        veiculo: Veiculo = Veiculo(*registro)
        print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Veiculo, Marca

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()

    comando: str = '''
        SELECT * FROM VEICULO
        JOIN MARCA ON MARCA.id = VEICULO.marca
    '''
    cursor.execute(comando)
    
    registros: list[tuple[str, str]] = cursor.fetchall()
    for registro in registros:
        print(registro)
        marca: Marca = Marca(*registro[6:])
        veiculo: Veiculo = Veiculo(*registro[:5], marca)
        print("Placa:", veiculo.placa, ", Marca:", veiculo.marca.nome)
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

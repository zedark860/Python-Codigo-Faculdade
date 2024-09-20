import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Veiculo

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    cursor: Cursor = conexao.cursor()

    comando: str = '''
        SELECT VEICULO.placa, VEICULO.ano, VEICULO.cor, VEICULO.motor, VEICULO.proprietario, MARCA.nome
        FROM VEICULO JOIN MARCA ON (MARCA.id = VEICULO.marca)
    '''
    cursor.execute(comando)
    
    reg_veiculos = cursor.fetchall()
    for reg_veiculo in reg_veiculos:
        veiculo: Veiculo = Veiculo(*reg_veiculo)
        print("Placa:", veiculo.placa, ", Marca:", veiculo.marca)
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

import sqlite3
import os
from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Marca, Veiculo

try:
    conexao: Connection = sqlite3.connect(os.getcwd() + "/database/meu_banco.db")
    
    # Habilita as chaves estrangeiras, pois o sqlite3 não suporta isso por padrão
    conexao.execute("PRAGMA foreign_keys = on")
    cursor: Cursor = conexao.cursor()

    comando1: str = '''
        INSERT INTO Marca (nome, sigla) 
        VALUES (:nome, :sigla);
    '''

    marca1: Marca = Marca("Marca A", "MA")
    cursor.execute(comando1, vars(marca1))
    marca1.id = cursor.lastrowid

    marca2 = Marca("Marca B", "MB")
    cursor.execute(comando1, vars(marca2))
    marca2.id = cursor.lastrowid

    comando2: str = '''
        INSERT INTO Veiculo
        VALUES (:placa, :ano, :cor, :motor, :proprietario, :marca)
    '''
                    
    veiculo1: Veiculo = Veiculo("AAA0001", 2001, "Prata", 1.0, 10000000099, marca1.id)
    veiculo2: Veiculo = Veiculo("BAA0002", 2002, "Preto", 1.4, 10000000099, marca1.id)
    veiculo3: Veiculo = Veiculo("CAA0003", 2003, "Branco", 2.0, 20000000099, marca2.id)
    veiculo4: Veiculo = Veiculo("DAA0004", 2004, "Azul", 2.2, 30000000099, marca2.id)
    cursor.execute(comando2, vars(veiculo1))
    cursor.execute(comando2, vars(veiculo2))
    cursor.execute(comando2, vars(veiculo3))
    cursor.execute(comando2, vars(veiculo4))

    conexao.commit()
except DatabaseError as erro:
    print("Erro de banco de dados", erro)
finally:
    if conexao and cursor:
        cursor.close()
        conexao.close()

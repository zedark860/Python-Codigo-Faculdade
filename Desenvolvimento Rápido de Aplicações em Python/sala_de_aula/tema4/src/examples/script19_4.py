from sqlite3 import Connection, Cursor, DatabaseError
from modelo import Veiculo, Marca

def recuperar_veiculos(conexao: Connection, cpf: str) -> list[Veiculo]:
    try:
        cursor: Cursor = conexao.cursor()

        comando: str = '''
            SELECT * FROM VEICULO
            JOIN MARCA ON MARCA.id = VEICULO.marca
            WHERE VEICULO.proprietario = ?
        '''
        cursor.execute(comando, (cpf,))
        
        veiculos: list[Veiculo] = []
        registros: list[tuple[str, str]] = cursor.fetchall()
        
        for registro in registros:
            marca: Marca = Marca(*registro[6:])
            veiculo: Veiculo = Veiculo(*registro[:5], marca)
            veiculos.append(veiculo)
            
        return veiculos
    except DatabaseError as erro:
        print("Erro de banco de dados", erro)
    finally:
        cursor.close()

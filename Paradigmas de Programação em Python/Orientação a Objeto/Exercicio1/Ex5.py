
class SistemaSeguranca:

    @staticmethod
    def determinar_acesso(value:int, name:str):
        if value >= 3:
            print(f"{name} pode entrar no sistema. Seu nível de acesso {value}")
        else:
            print(f"{name} não tem acesso ao sistema. Seu nível de acesso é abaixo de 3")

class Usuario:

    def __init__(self, nome:str, nivel_acesso:int):
        self.__nome: str = nome
        self.__nivel_acesso: int = nivel_acesso

    @property
    def nivel_acesso(self) -> int:
        return self.__nivel_acesso
    
    @property
    def nome(self) -> str:
        return self.__nome

if __name__ == "__main__":
    user = Usuario("Jorge", 3)
    sys_seguranca = SistemaSeguranca()
    sys_seguranca.determinar_acesso(user.nivel_acesso, user.nome)
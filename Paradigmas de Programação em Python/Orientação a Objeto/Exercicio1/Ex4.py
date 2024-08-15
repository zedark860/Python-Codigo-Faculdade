
class Funcionario:

    ultimo_id = 0

    def __init__(self, nome: str, salario: float):
        Funcionario.ultimo_id += 1
        self.__nome: str = nome
        self.__id: int = Funcionario.ultimo_id
        self.__salario: float = salario

    @property
    def salario(self) -> float:
        return self.__salario

    @salario.setter
    def salario(self, novo_salario: float) -> None:
        self.__salario = novo_salario

    def __str__(self) -> str:
        return f"O funcionário possui as seguintes informações:\n Nome = {self.__nome}\n Id = {self.__id}\n Salario = {self.salario}"
    
class Departamento:

    def __init__(self):
        self.__funcionarios = list()

    def listar_funcionarios(self) -> None:
        for funcionario in self.__funcionarios:
            print(funcionario)

    def adicionar_funcionario(self, funcionario: Funcionario) -> None:
        self.__funcionarios.append(funcionario)
            
    
if __name__ == "__main__":
    funcionario1 = Funcionario("Roberto", 1500.00)
    funcionario2 = Funcionario("Claudio", 1700.00)
    departamento = Departamento()
    departamento.adicionar_funcionario(funcionario1)
    departamento.adicionar_funcionario(funcionario2)
    departamento.listar_funcionarios()



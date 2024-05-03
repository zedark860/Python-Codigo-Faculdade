
class ContaBancaria:

    def __init__(self, saldo):
        self.__saldo: float = saldo

    def depositarSaldo(self, valor:float) -> None:
        self.__saldo += valor

    def retirarSaldo(self, valor:float) -> None:
        self.__saldo -= valor

    def exibirSaldo(self) -> None:
        print(f"Seu saldo atual é {self.__get_saldo}")

    @property
    def __get_saldo(self) -> float:
        return self.__saldo
    
if __name__ == "__main__":
    conta = ContaBancaria(1000.0)
    conta.depositarSaldo(500.0)
    conta.exibirSaldo()
    conta.retirarSaldo(200.0)
    conta.exibirSaldo()
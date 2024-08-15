
class Carro:

    def __init__(self, marca, modelo):
        self.marca: str = marca
        self.modelo: str = modelo

    def exibir_informacoes(self) -> str:
        return f"Informações do carro\n Marca: {self.marca}\n Modelo: {self.modelo}"
    
if __name__ == "__main__":
    carro = Carro("Lamborghini", "HURACÁN")
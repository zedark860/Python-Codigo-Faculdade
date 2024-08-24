from abc import ABC, abstractmethod

class Billable(ABC):
    
    @abstractmethod
    def generate_bill(self) -> str:
        pass
    

class Product(Billable):
    
    def __init__(self, name: str, unitary_price: float, quantity: int) -> None:
        self.name = name
        self.unitary_price = unitary_price
        self.quantity = quantity
    
    # aqui está uma maneira de implementar interface em Python
    # por conta que ao utilizar a classe abstrata
    # ela obriga a implementar o método, caso o contrário irá gerar um erro
    # exemplo abaixo:
    """Não é possível instanciar a classe abstrata "Service"
    "Billable.generate_bill" não está implementado"""
    def generate_bill(self) -> str:
        total: float = self.unitary_price * self.quantity
        return f"Fatura do Produto:\nNome: {self.name}\nQuantidade: {self.quantity}\nPreço Unitário: R${self.unitary_price:.2f}\nTotal: R${total:.2f}\n"
    
    
class Service(Billable):
    
    def __init__(self, description: str, hours: int, price_per_hour: float) -> None:
        self.description = description
        self.hours = hours
        self.price_per_hour = price_per_hour
        
    def generate_bill(self) -> str:
        total: float = self.hours * self.price_per_hour
        return f"Fatura do Serviço:\nDescrição: {self.description}\nHoras: {self.hours}\nPreço por Hora: R${self.price_per_hour:.2f}\nTotal: R${total:.2f}\n"
    
    
if __name__ == "__main__":
    product: Product = Product("Notebook", 1000.00, 2)
    print(product.generate_bill())
    
    service: Service = Service("Manutenção", 3, 50.00)
    print(service.generate_bill())
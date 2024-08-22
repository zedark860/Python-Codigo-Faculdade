from abc import ABC, abstractmethod

# fonte utiliza para montar o exercício: https://awari.com.br/guia-completo-para-dominar-a-classe-abstrata-em-python/

class Sale(ABC):
    
    @abstractmethod
    def total(self) -> float:
        pass
    
    @abstractmethod
    def details_exibition(self) -> None:
        pass
    

class ProductSale(Sale):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def total(self) -> float:
        return self.price * self.quantity
      
        
    def details_exibition(self) -> None:
        print(f"Nome: {self.name}\nPreço: {self.price}\nQuantidade: {self.quantity}\n")
        print(f"O total a pagar pelo produto é R${self.total()} reais")
        

class ServiceSale(Sale):
    def __init__(self, name: str, hours_quantity: int, price_per_hour: float) -> None:
        self.name = name
        self.hours_quantity = hours_quantity
        self.price_per_hour = price_per_hour
        
        
    def total(self) -> float:
        return self.hours_quantity * self.price_per_hour
      
        
    def details_exibition(self) -> None:
        print(f"Nome do Serviço: {self.name}\nTotal de gastas Horas: {self.hours_quantity}\nPreço por hora: {self.price_per_hour}\n")
        print(f"O total a pagar pelo serviço é R${self.total()} reais")
        

if __name__ == "__main__":
    productSale: ProductSale = ProductSale("Notebook", 1000.00, 2)
    productSale.details_exibition()
    
    serviceSale: ServiceSale = ServiceSale("Manutenção", 3, 50.00)
    serviceSale.details_exibition()
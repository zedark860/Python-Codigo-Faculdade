from datetime import date

class Product:
    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        
        
    def total(self) -> float:
        return self.price * self.quantity
      
        
class Eletronic(Product):
    def __init__(self, name: str, price: float, quantity: int, warranty: str) -> None:
        super().__init__(name, price, quantity)
        self.warranty = int(warranty) - date.today().year
        
        
    def exibition_details(self) -> None:
        print(f"Nome: {self.name}\nPreço: {self.price}\nQuantidade: {self.quantity}\nGarantia de {self.warranty} anos\n")
        print(f"O total de itens no estoque é de R${self.total()} reais")


class Food(Product):
    def __init__(self, name: str, price: float, quantity: int, expiration_date: str) -> None:
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    
    
    def exibition_details(self) -> None:
        print(f"Nome: {self.name}\nPreço: {self.price}\nQuantidade: {self.quantity}\nValidade: {self.expiration_date}\n")
        print(f"O total de itens no estoque é de R${self.total()} reais")
    
    
if __name__ == "__main__":
    eletronic: Eletronic = Eletronic("Teclado", 100.00, 10, "2026")
    eletronic.exibition_details()
    
    food: Food = Food("Arroz", 10.00, 10, "01/12/2025")
    food.exibition_details()
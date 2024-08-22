
class Car:
    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year
        
        
    def details(self) -> None:
        print(f"Detalhes do carro:\n marca = {self.brand} : modelo = {self.model} : ano = {self.year}")


if __name__ == "__main__":
    car1: Car = Car("BMW", "GTR M3", 1985)
    car2: Car = Car("NISSAN", "SKYLINE GTR R34", 1998)
    
    car1.details()
    car2.details()        
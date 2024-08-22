
class Address:
    def __init__(self, street: str, number: int, city: str) -> None:
        self.street = street
        self.number = number
        self.city = city
        
        
    def __str__(self) -> str:
        return f"{self.street}, {self.number}, {self.city}"
    
    
class Person(Address):
    def __init__(self, name: str, adress: Address) -> None:
        super().__init__(adress.street, adress.number, adress.city)
        self.name = name
       
        
    def exibition_address(self) -> None:
        print(f"Moro na {self.street}, {self.number}, {self.city}")
       
        
if __name__ == "__main__":
    person: Person = Person("Jhon", Address("rua que sobe e desce", 123, "São Paulo"))
    person.exibition_address()
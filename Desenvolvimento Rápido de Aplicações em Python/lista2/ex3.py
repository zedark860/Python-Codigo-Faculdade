
class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
        
    def greet(self) -> str:
        return f"Olá! Me chamo {self.name} e tenho {self.age}!"
        

class Employee(Person):
    def __init__(self, name: str, age: int, role: str) -> None:
        super().__init__(name, age)
        self.role = role
        
        
    def greet(self) -> str:
        return f"{super().greet()} Meu cargo é {self.role}"
       
        
if __name__ == "__main__":
    person: Person = Person("Jhon", 24)
    print(person.greet())
    
    employee: Employee = Employee("Jessica", 23, "Analista")
    print(employee.greet())
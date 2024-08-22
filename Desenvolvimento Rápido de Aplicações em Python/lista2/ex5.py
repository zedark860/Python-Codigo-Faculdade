from abc import ABC, abstractmethod

# fonte utiliza para montar o exercício: https://awari.com.br/guia-completo-para-dominar-a-classe-abstrata-em-python/


class Form(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass


class Rectangle(Form):
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        
        
    def area(self) -> float:
        return self.width * self.height


class Circle(Form):
    def __init__(self, radius: float) -> None:
        self.radius = radius
        
        
    def area(self) -> float:
        return 3.14 * (self.radius**2)
    
if __name__ == "__main__":
    rectangle: Rectangle = Rectangle(10, 5)
    print(rectangle.area())
    
    circle: Circle = Circle(10)
    print(circle.area())
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height
        
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    

rectangle: Rectangle = Rectangle(width=3, height=4)

print(rectangle.area())
print(rectangle.perimeter())
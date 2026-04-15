from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    def description(self):
        return "This is a geometric shape."
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
# shape = Shape() # This will raise an error because we cannot instantiate an abstract class

circle = Circle(5)
print(f"Area of circle with radius 5: {circle.area()}") #output: Area of circle
print(f"Description: {circle.description()}") #output: Description: This is a geometric shape.
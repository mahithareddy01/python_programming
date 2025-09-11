from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self): pass
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        return 3.14*self.r*self.r
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        return self.l*self.b

cir=Circle(5)
print("Area of circle is: ",cir.area())
rect=Rectangle(4,5)
print(f"Area of Rectangle is: {rect.area()}")
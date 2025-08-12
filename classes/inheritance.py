class Shape:
    def __init__(self, name):
        self.name = name


    def describe(self):
        print(f"This is a shape named {self.name}")

#shape1=Shape(name="Circle")
#shape1.describe()

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.width = width
        self.length = length

    def area(self):
        a = self.length * self.width
        print(f"for {self.name}, area is {a}")
        return a
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        a = 3.14 * (self.radius * self.radius)
        print(f"For {self.name}, area is {a}")
        return a

r1 = Rectangle(length=10, width=5)
r1.describe()
print(f"Length: {r1.length}, Width: {r1.width}")    
r1.area()

c1 = Circle(radius=7)
c1.describe()
print(f"Radius: {c1.radius}")
c1.area()
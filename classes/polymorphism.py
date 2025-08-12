 # polymorphism is when a method in a base class is overridden by a derived class, allowing for different behaviors based on the object type.
# In this example, we will create a base class Shape and derived classes Rectangle, Circle, and Triangle.
# Each derived class will implement its own area method.

class Shape:
    def __init__(self, name):
        self.name = name


    def describe(self):
        print(f"This is a shape named {self.name}")

    def area(self):
        print(f"for {self.name} area is not defined")#polymorphism(this will be used if a shape does not have an area method)
        return None

#shape1=Shape(name="Circle")
#shape1.describe()

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle") #super() calls the parent class's constructor
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
    
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height  

r1 = Rectangle(length=10, width=5)
r1.describe()
print(f"Length: {r1.length}, Width: {r1.width}")    
r1.area()

c1 = Circle(radius=7)
c1.describe()
print(f"Radius: {c1.radius}")
c1.area()

t1 = Triangle(base=5, height=10)
t1.describe()
print(f"Base: {t1.base}, Height: {t1.height}")
t1.area()  # This will call the area method from Shape, which does not compute an area
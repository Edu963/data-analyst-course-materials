'''   
Create a base class Shape with a method area.
Create derived classes Rectangle and Circle each with their own implementation of the area method.
Write a function that takes a Shape object and prints its area.
'''

class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width 
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
# Polymorphic function
def print_area(shape):
    print(shape.area())

# Create instances of Rectangle and Circle
rectangle = Rectangle(4, 5)
circle = Circle(3)

print_area(rectangle)  
print_area(circle)     
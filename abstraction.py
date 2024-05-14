from abc import ABC,abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    
    # method 1 to do the logic on concrete classes, create there instances and call the required logic
    @staticmethod 
    def get_area(shape_type,*args):
        if shape_type == 'rectangle':
            return Rectangle(*args).area()
        elif shape_type == 'square':
            return Square(*args).area()

class Rectangle(Shape):

    def __init__(self,l,b) -> None:
        self.l=l
        self.b=b

    def area(self):
        return f"area of rectangle {self.l*self.b}"

class Square(Shape):

    def __init__(self,l) -> None:
        self.l=l

    def area(self):
        return f"area of square {self.l*self.l}"


# method 2 to create factory classes
class ShapeFactory:

    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == 'rectangle':
            return Rectangle(*args)
        elif shape_type == 'square':
            return Square(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# driver code for factory method
def main():
    
    shapes = [
        ShapeFactory.create_shape('rectangle', 5, 4),
        ShapeFactory.create_shape('square', 5)
    ]
    
    for shape in shapes:
        print(shape.area())

# driver code for method 1
x= Shape.get_area("square",3)
print(x)
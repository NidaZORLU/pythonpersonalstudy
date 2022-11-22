from math import pi

class Circle:

    def __init__(self, radius=1.0):
        self.radius = radius  # Create an instance variable radius

    def __str__(self):
        return f'Radius of the circle is {self.radius}'

    def __repr__(self):
        return f'Radius of the circle is {self.radius}'

    def get_area(self):
        self.area = self.radius * self.radius * pi
        return self.area

#now testing
if __name__ == '__main__':
    circle1 = Circle(2.1)
    print(circle1)
    print(circle1.get_area())
    print(circle1.radius)
    print(str(circle1))
    print(repr(circle1))

    circle2 = Circle()
    print(circle2)
    print(circle2.get_area())

    circle2.color = 'red'
    print(circle2.color)

    print(__doc__)
    print(Circle.__doc__)
    print(Circle.get_area.__doc__)

    print(isinstance(circle1, Circle))
    print(isinstance(circle2, Circle))
    print(isinstance(circle1, str))

from math import pi
from circle import Circle

class Cylinder(Circle):

    def __init__(self, radius=1.0, height=1.0):
        super().__init__(radius)
        self.height = height

    def __str__(self):
        return f'Radius of the cylinder {super().__repr__()} and height of the cylinder is {self.height}'

    def __repr__(self):
        return self.__str__()
    #overriding
    def get_area(self):
        return 2.0 * pi * self.radius * self.height

    def get_volume(self):
        return super().get_area() * self.height


if __name__ == '__main__':
    cylinder1 = Cylinder(1.1, 2.2)
    print(cylinder1)
    print(cylinder1.get_area())
    print(cylinder1.get_volume())
    print(cylinder1.radius)
    print(cylinder1.height)
    print(str(cylinder1))
    print(repr(cylinder1))

    cylinder2 = Cylinder()
    print(cylinder2)
    print(cylinder2.get_area())
    print(cylinder2.get_volume())

    print(dir(cylinder1))
    print(Cylinder.get_area)
    print(Circle.get_area)

from math import pi


class Figure:
    def __init__(self, a):
        self.a = a


class Circle(Figure):

    def area(self):
        return pi * self.a ** 2

    def perimeter(self):
        return 2 * pi * self.a

    def diameter(self):
        return self.a * 2


class Square(Figure):
    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4

    def diagonal(self):
        return self.a * 2 ** 0.5


class Rectangle(Figure):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return self.a * 2 + self.b * 2

    def diagonal(self):
        return (self.a * 2 + self.b * 2) ** 0.5


class Triangle(Figure):
    def __init__(self, a, b, c):
        super().__init__(a)
        self.b = b
        self.c = c

    @staticmethod
    def perimeter(a, b, c):
        return a + b + c

    def area(self):
        pp = Triangle.perimeter(self.a, self.b, self.c) / 2
        return (pp * (pp - self.a) * (pp - self.b) * (pp - self.c)) ** 0.5

    def medians(self):
        return (2 * self.a ** 2 + 2 * self.b ** 2 - self.c ** 2) ** 0.5 / 2, (
                    2 * self.b ** 2 + 2 * self.c ** 2 - self.a ** 2) ** 0.5 / 2, (
                           2 * self.c ** 2 + 2 * self.a ** 2 - self.b ** 2) ** 0.5 / 2


class Trapezoid(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a)
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        return (self.a + self.c) / 2 * ((self.b ** 2 - ((self.c - self.a) ** 2 + self.b ** 2 - self.d ** 2) / (
                    2 * (self.c - self.a))) ** 0.5)

    def middle_line(self):
        return (self.a + self.c) / 2


class Rhombus(Figure):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def area(self):
        return self.a * self.b / 2

    def side(self):
        return ((self.a ** 2 + self.b ** 2) ** 0.5) / 2


class Sphere(Circle):
    def __init__(self, a):
        super().__init__(a)

    def area(self):
        return super().area() * 4

    def volume(self):
        return self.area()/3*self.a


class Cube(Square):
    def area(self):
        return super().area() * 6


# class Parallelepiped(Rectangle, Phombus )


# circle = Circle(3)
# print(circle.area())
# print(circle.perimeter())
# print(circle.radius())

# square = Square(3)
# print(square.area())
# print(square.perimeter())
# print(square.diagonal())

# rectagle = Rectangle(3, 4)
# print(rectagle.area())
# print(rectagle.perimeter())
# print(rectagle.diagonal())

# triagle = Triangle(3, 4, 5)
# print(triagle.area())
# print(triagle.perimeter())
# print(triagle.medians())

# trapezoid = Trapezoid(1, 2, 3, 2)
# print(trapezoid.area())
# print(trapezoid.middle_line())

# rhombus = Rhombus(1, 2)
# print(rhombus.area())
# print(rhombus.side())

sphere = Sphere(1)
print(sphere.volume())

# cube = Cube(1)
# print(cube.area())

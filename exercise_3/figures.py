from math import pi


class Figure:
    """Общий класс и атрибут для всех фигур"""
    def __init__(self, a):
        """Конструктор класса"""
        self.a = a


class Circle(Figure):
    """Круг"""
    tittle = 'Circle'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    @staticmethod
    def circle_area(a):
        """Площадь круга"""
        return pi * a ** 2

    def area(self):
        """Площадь круга"""
        return Circle.circle_area(self.a)

    def perimeter(self):
        """Периметр круга"""
        return 2 * pi * self.a

    def diameter(self):
        """Диаметр круга"""
        return self.a * 2


class Square(Figure):
    """Квадрат"""
    tittle = 'Square'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def area(self):
        """Площадь квадрата"""
        return self.a ** 2

    def perimeter(self):
        """Периметр квадрата"""
        return self.a * 4

    def diagonal(self):
        """Диагональ квадрата"""
        return self.a * 2 ** 0.5


class Rectangle(Figure):
    """Прямоугольник"""
    tittle = 'Rectangle'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b

    @staticmethod
    def rectangle_area(a, b):
        """Площадь прямоугольника"""
        return a * b

    @staticmethod
    def rectangle_diagonal(a, b):
        """Диагональ прямоугольника"""
        return (a ** 2 + b ** 2) ** 0.5

    def area(self):
        """Площадь прямоугольника"""
        return Rectangle.rectangle_area(self.a, self.b)

    def perimeter(self):
        """Периметр прямоугольника"""
        return self.a * 2 + self.b * 2

    def diagonal(self):
        """Диагональ прямоугольника"""
        diagonal = Rectangle.rectangle_diagonal(self.a, self.b)
        return diagonal


class Triangle(Figure):
    """Треугольник"""
    tittle = 'Triangle'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b, c):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b
        self.c = c

    @staticmethod
    def semi_perimeter(a, b, c):
        """Полупериметр треугольника"""
        return (a + b + c) / 2

    @staticmethod
    def triangle_area(a, b, c):
        """Площадь треугольника"""
        pp = Triangle.semi_perimeter(a, b, c)
        return (pp * (pp - a) * (pp - b) * (pp - c)) ** 0.5

    def area(self):
        """Площадь треугольника"""
        return Triangle.triangle_area(self.a, self.b, self.c)

    def medians(self):
        """Медианы треугольника"""
        return (2 * self.a ** 2 + 2 * self.b ** 2 - self.c ** 2) ** 0.5 / 2, (
                2 * self.b ** 2 + 2 * self.c ** 2 - self.a ** 2) ** 0.5 / 2, (
                       2 * self.c ** 2 + 2 * self.a ** 2 - self.b ** 2) ** 0.5 / 2


class Trapezoid(Figure):
    """Трапеция"""
    tittle = 'Trapezoid'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b, c, d):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        """Площадь трапеции"""
        return (self.a + self.c) / 2 * ((self.b ** 2 - ((self.c - self.a) ** 2 + self.b ** 2 - self.d ** 2) / (
                2 * (self.c - self.a))) ** 0.5)

    def middle_line(self):
        """Средняя линия трапеции"""
        return (self.a + self.c) / 2


class Rhombus(Figure):
    """Ромб"""
    tittle = 'Rhombus'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b

    def area(self):
        """Площадь ромба"""
        return self.a * self.b / 2

    def side(self):
        """Сторона ромба"""
        return ((self.a ** 2 + self.b ** 2) ** 0.5) / 2


class Sphere(Circle):
    """Сфера"""
    tittle = 'Sphere'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a):
        """Конструктор класса"""
        super().__init__(a)

    def area(self):
        """Площадь сферы"""
        return super().area() * 4

    def volume(self):
        """Объем сферы"""
        return self.area() / 3 * self.a


class Cube(Square):
    """Куб"""
    tittle = 'Cube'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a):
        """Конструктор класса"""
        super().__init__(a)

    def area(self):
        """Площадь куба"""
        return super().area() * 6

    def volume(self):
        """Объем куба"""
        return self.a ** 3


class Parallelepiped(Figure):
    """Прямоугольный параллелепипед"""
    tittle = 'Parallelepiped'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b, c):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b
        self.c = c

    def area(self):
        """Площадь параллелепипеда"""
        return self.a * self.b * 2 + self.b * self.c * 2 + self.a * self.c * 2

    def volume(self):
        """Объем параллелепипеда"""
        return self.a * self.b * self.c


class Pyramid(Figure):
    """Чутырехугольная пирамида"""
    tittle = 'Pyramid'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b, c):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b
        self.c = c

    @staticmethod
    def pyramid_height(a, b, c):
        """Высота пирамиды"""
        print((4 * (c ** 2) - Rectangle.rectangle_diagonal(a, b) ** 2) ** 0.5 / 2)
        return (4 * (c ** 2) - Rectangle.rectangle_diagonal(a, b) ** 2) ** 0.5 / 2

    def area(self):
        """Площадь пирамиды"""
        area_base = Rectangle.rectangle_area(self.a, self.b)
        side1 = Triangle.triangle_area(self.a, self.c, self.c)
        side2 = Triangle.triangle_area(self.b, self.c, self.c)
        return area_base + side1 * 2 + side2 * 2

    def volume(self):
        """Объем пирамиды"""
        h = Pyramid.pyramid_height(self.a, self.b, self.c)
        area = Rectangle.rectangle_area(self.a, self.b)
        return h * area / 3

class Cylinder(Circle):
    """Цилиндр"""
    tittle = 'Cylinder'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b

    def area(self):
        """Площадь цилиндра"""
        return 2 * Circle.circle_area(self.a) + 2 * pi * self.a * self.b

    def volume(self):
        """Объем цилиндра"""
        return Circle.circle_area(self.a) * self.b

class Cone(Circle):
    """Конус"""
    tittle = 'Cone'

    @classmethod
    def name(cls):
        """Выводим имя класса"""
        print(cls.tittle)

    def __init__(self, a, b):
        """Конструктор класса"""
        super().__init__(a)
        self.b = b

    @staticmethod
    def cone_side(a, b):
        """Боковая сторона конуса"""
        return pi * a * b

    def area(self):
        """Площадь конуса"""
        return Circle.circle_area(self.a) + pi * self.a * Cone.cone_side(self.a, self.b)

    def volume(self):
        """Объем конуса"""
        return Circle.circle_area(self.a) * self.b / 3




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

# sphere = Cube(2)
# print(sphere.volume())

# cube = Cube(1)
# print(cube.area())

# parallelepiped = Pyramid(3, 3, 3)
# print(parallelepiped.area())
# print(parallelepiped.volume())

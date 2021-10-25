from figures import *


def start_choice():
    choice = input('Если хотите вычислить параметры для ещё одной фигуры, то введите [да]:\n').upper()
    if choice == 'ДА':
        start = True
    else:
        start = False

    return start

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        print('Введено не число')
        return False

def check_plus(a):
    if a > 0:
        return True
    else:
        print(f'{a} меньше или равен 0')
        return False

def check_input(a):
    if is_number(a):
        if check_plus(float(a)):
            return True
        else:
            return False
    else:
        return False

def circle_input():
    a = input('Программа поддерживает вычисления площади и диаметра круга.\nДля получения результатов введите радиус '
              'круга:\n')
    if check_input(a):
        return float(a)
    else:
        return False

def circle_calc(a):
    circle = Circle(a)
    Circle.name()
    print(f'Площадь фигуры: {circle.area()}\nДиаметр круга: {circle.diameter()}')

def square_input():
    a = input(
        'Программа поддерживает вычисления площади и диагонали квадрата.\nДля получения результатов введите '
        'сторону квадрата:\n')
    if check_input(a):
        return float(a)
    else:
        return False

def square_calc(a):
    square = Square(a)
    Square.name()
    print(f'Площадь фигуры: {square.area()}\nДиагональ квадрата: {square.diagonal()}')

def rectangle_input():
    a = input(
        'Программа поддерживает вычисления площади и диагонали прямоугольника.\nДля получения результатов введите '
        'сначала первую сторону прямоугольника:\n')
    if check_input(a):
        b = input('Затем вторую:\n')
        if check_input(b):
            return float(a), float(b)
        else:
            return False, False
    else:
        return False, False

def rectangle_calc(a, b):
    rectangle = Rectangle(a, b)
    Rectangle.name()
    print(f'Площадь фигуры: {rectangle.area()}\nДиагональ прямоугольника: {rectangle.diagonal()}')

def triangle_input():
    a = input(
        'Программа поддерживает вычисления площади и медиан треугольника.\nДля получения результатов введите '
        'сначала первую сторону треугольника:\n')
    if check_input(a):
        b = input('Вторую:\n')
        if check_input(b):
            c = input('И третью:\n')
            if check_input(c):
                return float(a), float(b), float(c)
            else:
                return False, False, False
        else:
            return False, False, False
    else:
        return False, False, False

def triangle_calc(a, b, c):
    triangle = Triangle(a, b, c)
    Triangle.name()
    print(f'Площадь фигуры: {triangle.area()}\nМедианы треугольника: {triangle.medians()}')

def trapezoid_input():
    a = input(
        'Программа поддерживает вычисления площади и средней линии трапеции.\nДля получения результатов введите '
        'сначала верхнее основание трапеции:\n')
    if check_input(a):
        b = input('Одну боковую сторону:\n')
        if check_input(b):
            c = input('Нижнее основание:\n')
            if check_input(c):
                d = input('Вторую боковую сторону:\n')
                if check_input(d):
                    return float(a), float(b), float(c), float(d)
                else:
                    return False, False, False, False
            else:
                return False, False, False, False
        else:
            return False, False, False, False
    else:
        return False, False, False, False

def trapezoid_calc(a, b, c, d):
    trapezoid = Trapezoid(a, b, c, d)
    Trapezoid.name()
    print(f'Площадь фигуры: {trapezoid.area()}\nСредняя линия трапеции: {trapezoid.middle_line()}')

def rhombus_input():
    a = input(
        'Программа поддерживает вычисления площади и стороны ромба.\nДля получения результатов введите сначала '
        'первую диагональ ромба:\n')
    if check_input(a):
        b = input('Затем вторую:\n')
        if check_input(b):
            return float(a), float(b)
        else:
            return False, False
    else:
        return False, False

def rhombus_calc(a, b):
    rhombus = Rhombus(a, b)
    Rhombus.name()
    print(f'Площадь фигуры: {rhombus.area()}\nСторона ромба: {rhombus.side()}')

def sphere_input():
    a = input('Программа поддерживает вычисления площади и объема сферы.\nДля получения результатов введите '
                  'радиус сферы:\n')
    if check_input(a):
        return float(a)
    else:
        return False

def sphere_calc(a):
    sphere = Sphere(a)
    Sphere.name()
    print(f'Площадь фигуры: {sphere.area()}\nОбъем сферы: {sphere.volume()}')

def cube_input():
    a = input('Программа поддерживает вычисления площади и объема куба.\nДля получения результатов введите '
                  'сторону куба:\n')
    if check_input(a):
        return float(a)
    else:
        return False

def cube_calc(a):
    cube = Cube(a)
    Cube.name()
    print(f'Площадь фигуры: {cube.area()}\nОбъем куба: {cube.volume()}')

def parallelepiped_input():
    a = input('Программа поддерживает вычисления площади и объема прямоугольного параллелепипеда.\nДля '
                  'получения результатов введите длину первой стороны:\n')
    if check_input(a):
        b = input('Второй:\n')
        if check_input(b):
            c = input('Третьей:\n')
            if check_input(c):
                return float(a), float(b), float(c)
            else:
                return False, False, False
        else:
            return False, False, False
    else:
        return False, False, False

def parallelepiped_calc(a, b, c):
    parallelepiped = Parallelepiped(a, b, c)
    Parallelepiped.name()
    print(f'Площадь параллелепипеда: {parallelepiped.area()}\nОбъем параллелепипеда: {parallelepiped.volume()}')

def pyramid_input():
    a = input('Программа поддерживает вычисления площади и объема четырехугольной пирамиды.\nДля '
                  'получения результатов введите длину первой стороны основания:\n')
    if check_input(a):
        b = input('Второй:\n')
        if check_input(b):
            c = input('И боковой стороны:\n')
            if check_input(c):
                return float(a), float(b), float(c)
            else:
                return False, False, False
        else:
            return False, False, False
    else:
        return False, False, False

def pyramid_calc(a, b, c):
    pyramid = Pyramid(a, b, c)
    Pyramid.name()
    print(f'Площадь параллелепипеда: {pyramid.area()}\nОбъем параллелепипеда: {pyramid.volume()}')

def cylinder_input():
    a = input('Программа поддерживает вычисления площади и объема цилиндра.\nДля получения результатов '
                  'введите радиус основания:\n')
    if check_input(a):
        b = input('И высоту:\n')
        if check_input(b):
            return float(a), float(b)
        else:
            return False, False
    else:
        return False, False

def cylinder_calc(a, b):
    cylinder = Cylinder(a, b)
    Cylinder.name()
    print(f'Площадь цилиндра: {cylinder.area()}\nОбъем цилиндра: {cylinder.volume()}')

def cone_input():
    a = input('Программа поддерживает вычисления площади и объема конуса.\nДля получения результатов введите '
                  'радиус основания:\n')
    if check_input(a):
        b = input('И высоту:\n')
        if check_input(b):
            return float(a), float(b)
        else:
            return False, False
    else:
        return False, False

def cone_calc(a, b):
    cone = Cone(a, b)
    Cone.name()
    print(f'Площадь цилиндра: {cone.area()}\nОбъем цилиндра: {cone.volume()}')


start = True

while start:
    choice = input(
        'Выберете фигуру для вычислений:\n1. Круг;\n2. Квадрат;\n3. Прямоугольник;\n4. Треугольник;\n5. Трапеция;\n6. '
        'Ромб;\n7. Сфера;\n8. Куб;\n9. Прямоугольный параллелепипед;\n10. Четырехугольная пирамида;\n11. '
        'Цилиндр;\n12. Конус.\n')
    if choice == '1':
        a = False
        while not a:
            a = circle_input()
        circle_calc(a)
        start = start_choice()
    elif choice == '2':
        a = False
        while not a:
            a = square_input()
        square_calc(a)
        start = start_choice()
    elif choice == '3':
        a, b = False, False
        while not a or not b:
            a, b = rectangle_input()
        rectangle_calc(a, b)
        start = start_choice()
    elif choice == '4':
        a, b, c = False, False, False
        while not a or not b or not c:
            a, b, c = triangle_input()
        triangle_calc(a, b, c)
        start = start_choice()
    elif choice == '5':
        a, b, c, d = False, False, False, False
        while not a or not b or not c or not d:
            a, b, c, d = trapezoid_input()
        trapezoid_calc(a, b, c, d)
        start = start_choice()
    elif choice == '6':
        a, b = False, False
        while not a or not b:
            a, b = rhombus_input()
        rhombus_calc(a, b)
        start = start_choice()
    elif choice == '7':
        a = False
        while not a:
            a = sphere_input()
        sphere_calc(a)
        start = start_choice()
    elif choice == '8':
        a = False
        while not a:
            a = cube_input()
        cube_calc(a)
        start = start_choice()
    elif choice == '9':
        a, b, c = False, False, False
        while not a or not b or not c:
            a, b, c = parallelepiped_input()
        parallelepiped_calc(a, b, c)
        start = start_choice()
    elif choice == '10':
        a, b, c = False, False, False
        while not a or not b or not c:
            a, b, c = pyramid_input()
        pyramid_calc(a, b, c)
        start = start_choice()
    elif choice == '11':
        a, b = False, False
        while not a or not b:
            a, b = cylinder_input()
        cylinder_calc(a, b)
        start = start_choice()
    elif choice == '12':
        a, b = False, False
        while not a or not b:
            a, b = cone_input()
        cone_calc(a, b)
        start = start_choice()

from figures import Circle, Square, Rectangle, Triangle, Trapezoid, Rhombus, Sphere, Cube


def start_choice():
    choice = input('Если хотите вычислить параметры для ещё одной фигуры, то введите [да]:\n').upper()
    if choice == 'ДА':
        start = True
    else:
        start = False

    return start


start = True

while start:
    choice = input(
        'Выберете фигуру для вычислений:\n1. Круг;\n2. Квадрат;\n3. Прямоугольник;\n4. Треугольник;\n5. Трапеция;\n6. '
        'Ромб;\n7. Сфера;\n8. Куб.\n')
    if choice == '1':
        a = int(input(
            'Программа поддерживает вычисления площади и диаметра круга.\nДля получения результатов введите радиус '
            'круга:\n'))
        circle = Circle(a)
        print(f'Площадь фигуры: {circle.area()}\nДиаметр круга: {circle.diameter()}')
        start = start_choice()
    elif choice == '2':
        a = int(input(
            'Программа поддерживает вычисления площади и диагонали квадрата.\nДля получения результатов введите '
            'сторону квадрата:\n'))
        square = Square(a)
        print(f'Площадь фигуры: {square.area()}\nДиагональ квадрата: {square.diagonal()}')
        start = start_choice()
    elif choice == '3':
        a = int(input(
            'Программа поддерживает вычисления площади и диагонали прямоугольника.\nДля получения результатов введите '
            'сначала первую сторону прямоугольника:\n'))
        b = int(input('Затем вторую:\n'))
        rectangle = Rectangle(a, b)
        print(f'Площадь фигуры: {rectangle.area()}\nДиагональ прямоугольника: {rectangle.diagonal()}')
        start = start_choice()
    elif choice == '4':
        a = int(input(
            'Программа поддерживает вычисления площади и медиан треугольника.\nДля получения результатов введите '
            'сначала первую сторону треугольника:\n'))
        b = int(input('Вторую:\n'))
        c = int(input('И третью:\n'))
        triangle = Triangle(a, b, c)
        print(f'Площадь фигуры: {triangle.area()}\nМедианы треугольника: {triangle.medians()}')
        start = start_choice()
    elif choice == '5':
        a = int(input(
            'Программа поддерживает вычисления площади и средней линии трапеции.\nДля получения результатов введите '
            'сначала верхнее основание трапеции:\n'))
        b = int(input('Одну боковую сторону:\n'))
        c = int(input('Нижнее основание:\n'))
        d = int(input('Вторую боковую сторону:\n'))
        trapezoid = Trapezoid(a, b, c, d)
        print(f'Площадь фигуры: {trapezoid.area()}\nСредняя линия трапеции: {trapezoid.middle_line()}')
        start = start_choice()
    elif choice == '6':
        a = int(input(
            'Программа поддерживает вычисления площади и стороны ромба.\nДля получения результатов введите сначала '
            'первую диагональ ромба:\n'))
        b = int(input('Затем вторую:\n'))
        rhombus = Rhombus(a, b)
        print(f'Площадь фигуры: {rhombus.area()}\nСторона ромба: {rhombus.side()}')
        start = start_choice()
    elif choice == '7':
        a = int(input(
            'Программа поддерживает вычисления площади и объема сферы.\nДля получения результатов введите радиус '
            'сферы:\n'))
        sphere = Sphere(a)
        print(f'Площадь фигуры: {sphere.area()}\nОбъем сферы: {sphere.volume()}')
        start = start_choice()
    elif choice == '8':
        a = int(input(
            'Программа поддерживает вычисления площади поверхности куба.\nДля получения результатов введите сторону '
            'куба:\n'))
        cube = Cube(a)
        print(f'Площадь фигуры: {cube.area()}')
        start = start_choice()

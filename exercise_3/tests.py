import unittest
from figures import Circle, Square, Rectangle, Triangle, Trapezoid, Rhombus, Sphere, Cube

class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(1)

    def test_area(self):
        self.assertEqual(self.circle.area(), 3.141592653589793)

    def test_diameter(self):
        self.assertEqual(self.circle.diameter(), 2)

class TestSquare(unittest.TestCase):
    def setUp(self):
        self.square = Square(1)

    def test_area(self):
        self.assertEqual(self.square.area(), 1)

    def test_diagonal(self):
        self.assertEqual(self.square.diagonal(), 1.4142135623730951)

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(1, 2)

    def test_area(self):
        self.assertEqual(self.rectangle.area(), 2)

    def test_diagonal(self):
        self.assertEqual(self.rectangle.diagonal(), 2.449489742783178)

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(3, 4, 5)

    def test_area(self):
        self.assertEqual(self.triangle.area(), 6.0)

    def test_medians(self):
        self.assertEqual(self.triangle.medians(), (2.5, 4.272001872658765, 3.605551275463989))

class TestTrapezoid(unittest.TestCase):
    def setUp(self):
        self.trapezoid = Trapezoid(1, 2, 3, 2)

    def test_area(self):
        self.assertEqual(self.trapezoid.area(), 3.4641016151377544)

    def test_middle_line(self):
        self.assertEqual(self.trapezoid.middle_line(), 2.0)

class TestRhombus(unittest.TestCase):
    def setUp(self):
        self.rhombus = Rhombus(1, 2)

    def test_area(self):
        self.assertEqual(self.rhombus.area(), 1.0)

    def test_side(self):
        self.assertEqual(self.rhombus.side(), 1.118033988749895)

class TestSphere(unittest.TestCase):
    def setUp(self):
        self.sphere = Sphere(1)

    def test_area(self):
        self.assertEqual(self.sphere.area(), 12.566370614359172)

    def test_volume(self):
        self.assertEqual(self.sphere.volume(), 4.1887902047863905)

class TestCube(unittest.TestCase):
    def setUp(self):
        self.cube = Cube(1)

    def test_area(self):
        self.assertEqual(self.cube.area(), 6)

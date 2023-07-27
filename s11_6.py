# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения
class Rectangle:
    """About class"""
    def __init__(self, width: float, heigth: float = None):
        """Added the width and heigth parameters."""
        self.width = width
        if heigth is None:
            self.heigth = width
        else:
            self.heigth = heigth

    def calc_perimeter(self):
        """Example of a perimeter."""
        return (self.width + self.heigth) * 2

    def calc_area(self):
        """Example of an area."""
        return self.heigth * self.width

    def __add__(self, other):
        perimeter = self.calc_perimeter() + other.calc_perimeter()
        width = self.width + other.width
        heigth = perimeter/2 - width
        return Rectangle(width, heigth)

    def __sub__(self, other):
        if self.calc_perimeter() < other.calc_perimeter():
            self, other = other, self
        perimeter = self.calc_perimeter() - other.calc_perimeter()
        width = abs(self.width - other.width)
        heigth = perimeter / 2 - width
        return Rectangle(width, heigth)

    def __str__(self):
        return f'Периметр = {self.calc_perimeter()}, ширина = {self.width}, высота = {self.heigth}'

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __lt__(self, other):
        return self.calc_area() < other.calc_area()

    def __le__(self, other):
        return self.calc_area() >= other.calc_area()


rez = Rectangle(5,20)
rez1 = Rectangle(10,2)
print(rez > rez1)
print(Rectangle.__doc__)
print(rez1.__init__.__doc__)
print(rez.calc_perimeter.__doc__)
print(rez.calc_area.__doc__)

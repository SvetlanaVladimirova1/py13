# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

class Rectangle:
    """Информация о классе Rectangle"""
    def __init__(self, width: float, heigth: float = None):
        """Добавили параметры высота и ширина."""
        self.width = width
        if heigth is None:
            self.heigth = width
        else:
            self.heigth = heigth

    def calc_perimeter(self):
        """Вычисляем периметр"""
        return (self.width + self.heigth) * 2

    def calc_area(self):
        """Вычисляем площадь"""
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


rez = Rectangle(10,20)
rez1 = Rectangle(10,2)
print(rez - rez1)
print(Rectangle.__doc__)
print(rez1.__init__.__doc__)
print(rez.calc_perimeter.__doc__)
print(rez.calc_area.__doc__)

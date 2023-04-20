
class Area:
    def calculate(self, l, w):
        return l*w


class Perimeter:
    def calculate(self, l, w):
        return (l+w)*2


class Rectangle:
    def __init__(self, l, w, calculation):
        self.l = l
        self.w = w
        self.calculation = calculation

    def calculate(self):
        return self.calculation.calculate(self.l, self.w)


s = Rectangle(5, 7, Area())
print(s.calculate())

p = Rectangle(57, 34, Perimeter())
print(p.calculate())

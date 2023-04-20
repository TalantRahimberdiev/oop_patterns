
class Presentation:
    def __str__(self):
        return self.__class__.__name__


class House(Presentation):
    def accept(self, visitor):
        return visitor.visit(self)

    def make_electricity(self, electrician):
        print(f'{self} checked by {electrician}')


class Electrician(Presentation):
    def visit(self, house):
        return house.make_electricity(self)


house = House()
electrician = Electrician()
house.accept(electrician)

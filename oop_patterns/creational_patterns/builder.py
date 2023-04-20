
class Product:
    def __init__(self):
        self.parts = list()

    def add_a(self):
        self.parts.append('a')

    def add_b(self):
        self.parts.append('b')

    def get_result(self):
        return self.parts


class Builder:
    def __init__(self):
        self.product = Product()

    def build(self):
        self.product.add_a()
        self.product.add_b()
        return self.product.parts


class Developer:
    def __init__(self):
        self.builder = Builder()

    def develop(self):
        return self.builder.build()


developer = Developer()
print(developer.develop())

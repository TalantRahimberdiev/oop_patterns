
class Product:
    def __init__(self, price, percent=0, strategy=None):
        self.price = price
        self.percent = percent
        self.strategy = strategy

    def get_discounted_price(self):
        if self.strategy:
            return self.strategy(self)

    def __repr__(self):
        statement = ''
        if self.percent and self.strategy:
            statement = 'real price:{}, discount:{}%, discounted_price:{}'
            statement = statement.format(
                self.price, self.percent, self.get_discounted_price())
        else:
            statement = 'real price:{}'
            statement = statement.format(self.price)
        return statement


def calculate_discounted_price(order):
    if order.percent and order.strategy:
        return order.price - int(order.price * order.percent / 100)


incir = Product(200, 20, strategy=calculate_discounted_price)
print(incir)

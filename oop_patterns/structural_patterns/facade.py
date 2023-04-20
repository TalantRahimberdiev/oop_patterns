
class Washing:
    def wash(self):
        return 'washes'


class Rinsing:
    def rinse(self):
        return 'rinses'


class Spinning:
    def spin(self):
        return 'spins'


class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def work(self):
        print(self.washing.wash(), self.spinning.spin(), self.rinsing.rinse())


washing_machine = WashingMachine()
washing_machine.work()

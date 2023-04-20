
class Leaf:
    def __init__(self, position):
        self.position = position

    def show_details(self):
        print('\t', end='')
        print(self.position)


class Composite:
    def __init__(self, position):
        self.position = position
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def show_details(self):
        print(self.position)
        for child in self.children:
            print('\t', end='')
            child.show_details()


director = Composite('director')
it_manager = Composite('it_manager')
finance_manager = Composite('finance_manager')

dsa = Leaf('data structures and algorithms')
analyst = Leaf('analyst')

accountant = Leaf('accountant')

director.add_child(it_manager)
director.add_child(finance_manager)

it_manager.add_child(dsa)
it_manager.add_child(analyst)

finance_manager.add_child(accountant)

director.show_details()

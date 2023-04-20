

class Mediator:
    def __init__(self):
        self.collegue_1 = Collegue1()
        self.collegue_2 = Collegue2()

    def get_collegue_1_method(self):
        return self.collegue_1.get_collegue_1_data()

    def get_collegue_2_method(self):
        return self.collegue_2.get_collegue_2_data()


class Collegue1:
    def __init__(self):
        self.name = 'collegue_1'

    def get_collegue_1_data(self):
        return self.name


class Collegue2:
    def __init__(self):
        self.name = 'collegue_2'

    def get_collegue_2_data(self):
        return self.name


mediator = Mediator()
for_collegue_1 = mediator.collegue_2.get_collegue_2_data()
print(for_collegue_1)

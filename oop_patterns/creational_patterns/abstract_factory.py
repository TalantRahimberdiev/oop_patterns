import random


class DSA:
    def check_title(self):
        return 'data structures and algorithms'

    def __str__(self):
        return 'DSA'


class SDE:
    def check_title(self):
        return 'software development engineer'

    def __str__(self):
        return 'SDE'


def random_choice():
    return random.choice([DSA, SDE])()


class Abstract_factory:
    def __init__(self, factory):
        self.factory = factory()

    def retrieve_data(self):
        print(self.factory)
        print(self.factory.check_title())


course = Abstract_factory(random_choice)
course.retrieve_data()

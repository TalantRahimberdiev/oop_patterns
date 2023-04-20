
class Iterable:
    def __init__(self, aggregates):
        self.index = 0
        self.aggregates = aggregates

    def next(self):
        if self.index < len(self.aggregates):
            aggregate = self.aggregates[self.index]
            self.index += 1
            return aggregate

    def has_next(self):
        return self.index < len(self.aggregates)


lst = [1, 2, 3, 4, 5]
iterable = Iterable(lst)
while(iterable.has_next()):
    print(iterable.next())

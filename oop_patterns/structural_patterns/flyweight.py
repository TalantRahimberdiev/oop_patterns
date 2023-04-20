
class Grade:
    _instances = {}

    def __new__(cls, percent):
        letter = 'ABCD'[percent]
        self = cls._instances.get(letter)
        if self is None:
            self = cls._instances[letter] = object.__new__(Grade)
            self.letter = letter
        return self

    def __repr__(self):
        return 'Grade {!r}'.format(self.letter)


print(Grade(0), Grade(1), Grade(2), Grade(3))
print(len(Grade._instances))    # number of instances
print(Grade(0) is Grade(1))  # ask for ‘A’ two more times
print(len(Grade._instances))    # number stayed the same?

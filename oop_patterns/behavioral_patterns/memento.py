
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class Writer:
    def __init__(self, file):
        self.file = file
        self.content = ''

    def write(self, chars):
        self.content += chars

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class CareTaker:

    def save(self, editor):
        self.obj = editor.save()

    def undo(self, editor):
        return editor.undo(self.obj)


writer = Writer('tmp.txt')
writer.write('initial text')
care_taker = CareTaker()
care_taker.save(writer)
writer.write('afterwards text')
print(writer.content)
print(care_taker.obj.content)

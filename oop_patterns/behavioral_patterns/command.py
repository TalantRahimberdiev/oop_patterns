
class Command:
    def __init__(self, performer):
        self.performer = performer

    def process(self):
        return self.performer.perform()


class Invoker:
    def __init__(self, cmd):
        self.cmd = cmd

    def invoke(self):
        return self.cmd.process()


class Performer:

    def perform(self):
        return 'action performed in performer'


performer = Performer()
command = Command(performer)
invoker = Invoker(command)
print(invoker.invoke())

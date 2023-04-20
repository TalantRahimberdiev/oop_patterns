
class Written:
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class Italic(Written):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return f'<i>{self.wrapped.render()}</i>'


class Underline(Written):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return f'<u>{self.wrapped.render()}</u>'


class Bold(Written):
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return f'<b>{self.wrapped.render()}</b>'


before = Written('decorator')
after = Italic(Underline(Bold(before)))
print(before.render())
print(after.render())

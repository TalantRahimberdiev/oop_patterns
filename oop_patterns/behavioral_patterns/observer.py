
class Observable:
    def __init__(self):
        self.observers = set()

    def subscribe(self, observer):
        self.observers.add(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def notify(self, *args):
        for observer in self.observers:
            observer.notify(*args)


class Observer:
    def __init__(self, observable):
        observable.subscribe(self)

    def notify(self, args):
        print(id(self), args)


observable = Observable()
observer_a = Observer(observable)
observer_b = Observer(observable)

observable.notify('alfa-1993')

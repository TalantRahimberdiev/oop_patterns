
class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f'{self.name}: {self.stations[self.pos]}')


class FM(State):
    def __init__(self, radio):
        self.name = 'FM'
        self.radio = radio
        self.pos = 0
        self.stations = [101, 103, 105]

    def toggle_amfm(self):
        self.radio.state = self.radio.am


class AM(State):
    def __init__(self, radio):
        self.name = 'AM'
        self.radio = radio
        self.pos = 0
        self.stations = [3101, 3103, 3105]

    def toggle_amfm(self):
        self.radio.state = self.radio.fm


class Radio:
    def __init__(self):
        self.am = AM(self)
        self.fm = FM(self)
        self.state = self.am

    def toggle_amfm(self):
        self.state.toggle_amfm()
        print(f'switching to: {self.state.name}')

    def scan(self):
        self.state.scan()


radio = Radio()
radio.scan()
radio.scan()
radio.scan()
radio.scan()

radio.toggle_amfm()
radio.scan()
radio.scan()
radio.scan()
radio.scan()


# second option


class State:

    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print(f'{self.name}: {self.stations[self.pos]}')


class FM(State):
    def __init__(self):
        self.name = 'FM'
        self.stations = [101, 103, 107]
        self.pos = 0


class AM(State):
    def __init__(self):
        self.name = 'AM'
        self.stations = [3101, 3103, 3107]
        self.pos = 0


class Radio:
    def __init__(self):
        self.am = AM()
        self.fm = FM()
        self.state = self.am

    def toggle_amfm(self):
        if self.state.name == 'AM':
            self.state = self.fm
        else:
            self.state = self.am
        print(f'switching to {self.state.name}')

    def scan(self):
        self.state.scan()


radio = Radio()
radio.scan()
radio.scan()

radio.toggle_amfm()
radio.scan()
radio.scan()

radio.toggle_amfm()
radio.scan()
radio.scan()

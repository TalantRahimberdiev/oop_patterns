
import copy


class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Singlton(Borg):
    def __init__(self, **kwargs):
        self._shared_state.update(kwargs)

    def __repr__(self):
        return str(self._shared_state)


class Proxy:
    def __init__(self):
        self.cache = {}
        self.singlton = Singlton()

    def get_ports(self):
        if self.cache == self.singlton._shared_state:
            print('ports from cache')
            return self.cache
        self.cache = copy.deepcopy(self.singlton._shared_state)
        print('ports from singlton')
        return self.cache


singlton = Singlton(django=8000, postgre=5432)
proxy = Proxy()
proxy.get_ports()
proxy.get_ports()

singlton = Singlton(mysql=3306)
proxy.get_ports()
proxy.get_ports()

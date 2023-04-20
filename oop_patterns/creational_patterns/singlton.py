
class Borg:
    _shared_state = dict()

    def __init__(self):
        self.__dict__ = self._shared_state


class Singlton(Borg):
    def __init__(self, **kwargs):
        self._shared_state.update(kwargs)

    def check_state(self):
        print(self._shared_state)


s = Singlton(dsa='data structures and algorithms')
s = Singlton(ml='machine learning')
s.check_state()


import copy


class API:
    def __init__(self, port):
        self.port = port

    def __str__(self) -> str:
        return str(self.port)


class Prototype:
    def __init__(self):
        self.objs = {}

    def register(self, key, obj):
        self.objs[key] = obj

    def unregister(self, key):
        del self.objs[key]

    def clone(self, key, **kwargs):
        obj = copy.deepcopy(self.objs[key])
        obj.__dict__.update(kwargs)
        return obj

    def get_prototypes(self):
        [print(key, ':', self.objs[key]) for key in self.objs]


django = API(8000)
prototype = Prototype()
prototype.register('django', django)
postgre = prototype.clone('django', port=5432)
prototype.register('postgre', postgre)
prototype.get_prototypes()


class Latin:

    def translate_into_latin(self):
        return 'notitia'


class Turkish:

    def translate_into_turkish(self):
        return 'bilgi'


class Adapter:
    def __init__(self, obj, **kwargs):
        self.obj = obj
        self.__dict__.update(kwargs)


lt = Latin()
tr = Turkish()

objs = [Adapter(lt, adapted=lt.translate_into_latin),
        Adapter(tr, adapted=tr.translate_into_turkish)]

for obj in objs:
    print(obj.adapted())


class Latin:
    def __init__(self):
        self.translations = {'database': 'database', 'information': 'notitia'}

    def translate(self, word):
        return self.translations.get(word)


class Turkish:
    def __init__(self):
        self.translations = {'database': 'veri tabani', 'information': 'bilgi'}

    def translate(self, word):
        return self.translations.get(word)


def Factory(language):
    languages = {'lat': Latin, 'tr': Turkish}
    return languages.get(language)()


latin = Factory('lat')
print(latin.translate('information'))

turkish = Factory('tr')
print(turkish.translate('information'))


class AbstractHandler:
    def __init__(self, succesor):
        self.succesor = succesor

    def handle(self, request):
        handler = self.operate_request(request)
        if not handler:
            self.succesor.handle(request)


class ConcreteHandlerOnes(AbstractHandler):

    def operate_request(self, request):
        if 0 < request < 10:
            print(request, self.__class__.__name__)
            return True


class ConcreteHandlerTens(AbstractHandler):

    def operate_request(self, request):
        if 9 < request < 100:
            print(request, self.__class__.__name__)
            return True


class ConcreteHandlerDefault(AbstractHandler):

    def operate_request(self, request):
        print(request, self.__class__.__name__)
        return True


class Client:
    def __init__(self):
        self.handler = ConcreteHandlerOnes(
            ConcreteHandlerTens(ConcreteHandlerDefault(None)))

    def execute(self, requests):
        for request in requests:
            self.handler.handle(request)


client = Client()
client.execute([80, 85, 89, 93, 1993, 1])

from twisted.web import server, resource
from twisted.internet import reactor


class Counter(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text-plain")
        return "I am request #" + str(self.numberRequests) + "\n"


def main():
    reactor.listenTCP(8080, server.Site(Counter()))
    reactor.run()


if __name__ == "__main__":
    main()
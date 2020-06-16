# -*- coding: utf-8 -*-


from twisted.internet import protocol, reactor


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


def main():
    reactor.listenTCP(8000, EchoFactory())
    reactor.run()


if __name__ == "__main__":
    main()
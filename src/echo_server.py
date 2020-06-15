# -*- coding: utf-8 -*-


from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        # echo 클라이언트로부터 바이트 형태의 데이터를 받는 함수
        self.transport.write(data + "!!!".encode())


class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        # Echo 함수를 반환하는(객체 아닌가?).. 프로토콜 팩토리 함수
        return Echo()


def main():
    endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())
    reactor.run()


if __name__ == "__main__":
    main()
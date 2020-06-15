# -*- coding: utf-8 -*-
"""
# Protocol
- 프로토콜 파싱, 핸들링을 담당하는 클래스
- 서버에 연결될 때 초기화되며, 연결이 끝나면 소멸

# Factory
- 환경 설정이 저장되는 클래스
- 기본 Factory 클래스는 Protocol 클래스 객체를 생성하여, 해당 객체의 factory 변수가 그 Factory 클래스를 가리키도록 한다.
- Protocol 클래스에 접근하고, 환경 설정을 할 수 있게 된다.
"""
from twisted.internet import reactor, protocol


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.transport.write("Hello, world!")

    def dataReceived(self, data):
        print "Server said:", data
        self.transport.loseConnection()


class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print "Connection failed."
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "Connection lost."
        reactor.stop()


def main():
    reactor.connectTCP("localhost", 8000, EchoFactory())
    reactor.run()


if __name__ == "__main__":
    main()

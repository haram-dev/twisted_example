from twisted.internet import reactor
from twisted.web.resource import Resource
from twisted.web.server import Site

import time


class ClockPage(Resource):
    isLeaf = True

    # 지원할 HTTP 메서드마다 'render_'를 접두어로 하는 메서드를 구현해야 함
    # -> 아래 메서드는 GET 요청을 처리하는 메서드
    # 클라이언트에서 보낸 요청이 매개변수로 전달됨
    # -> twisted.web.server.Request 인스턴스로, 세션 관리와 렌더링과 같은 애플리케이션 계층을 이해함
    def render_GET(self, request):
        return "The local time is %s" % (time.ctime(),)


resource = ClockPage()
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()
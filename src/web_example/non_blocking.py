from twisted.internet import reactor
from twisted.internet.task import deferLater
from twisted.web.resource import Resource
from twisted.web.server import Site, NOT_DONE_YET

import time


class BusyPage(Resource):
    isLeaf = True

    def _delayedRender(self, request):
        request.write("Finally done, at %s" % (time.asctime(),))
        request.finish()

    def render_GET(self, request):
        # 5초 후에 점화되는 deferred
        d = deferLater(reactor, 5, lambda: request)
        # 5초 후 (자원이 사용 가능해졌을 때) 요청을 완료하기 위해 콜백 등록
        d.addCallback(self._delayedRender)
        # 자원을 기다리지 않고 즉시 값을 반환하기 때문에 웹 서버는 다른 요청들을 처리할 수 있음
        return NOT_DONE_YET


factory = Site(BusyPage())
reactor.listenTCP(8000, factory)
reactor.run()
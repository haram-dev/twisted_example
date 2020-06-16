from twisted.internet import reactor, defer


class HeadlineRetriever(object):
    def processHeadline(self, headline):
        if len(headline) > 50:
            self.d.errback("The headline ''%s'' is too long!" % (headline,))
        else:
            self.d.callback(headline)

    def _toHTML(self, result):
        return "<h1>%s</h1>" % (result,)

    def getHeadline(self, input):
        self.d = defer.Deferred()
        # 이벤트 스케줄링
        # 1초 후에 (가짜) 비동기식 이벤트가 도착하도록 함
        reactor.callLater(1, self.processHeadline, input)
        self.d.addCallback(self._toHTML)
        return self.d

    def printData(self, result):
        print result
        reactor.stop()

    def printError(self, failure):
        print failure
        reactor.stop()


h = HeadlineRetriever()
d = h.getHeadline("Breaking News: Twisted Takes Us to the Moon!")
d.addCallbacks(h.printData, h.printError)

reactor.run()


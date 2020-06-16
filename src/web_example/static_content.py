from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.static import File

resource = File('/var/www/mysite')
# Site 객체가 reactor에 등록되어 8000번 포트에서 요청을 listen 함
factory = Site(resource)
reactor.listenTCP(8000, factory)
reactor.run()
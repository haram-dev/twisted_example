from twisted.internet.defer import Deferred

def myCallback(result):
    print result

# Deferred 생성
d = Deferred()
# 콜백 체인에 myCallback 함수 등록
d.addCallback(myCallback)
# 생성한 Deferred를 점화(fire)하여 콜백 체인의 첫 번째 함수를 호출
# 현재는 콜백 체인에 등록된 함수가 하나(myCallback)인 상태
d.callback("Triggering callback.")


# -*- coding: utf-8 -*-
from twisted.internet.defer import Deferred

def myErrback(failure):
    print failure


# Deferred 생성
d = Deferred()
# 에러백 체인에 함수 등록
d.addErrback(myErrback)
# 생성한 Deferred를 점화시키고, 에러백 체인에 있는 첫 번째 함수를 호출함
# 에러백에 전달될 매개변수는 에러백 함수로 전달되기 전에 실패(Failure) 객체로 wrapping 됨
# Failure: twisted의 예외(Exception) 구현체로, 비동기식 통신에 적합하도록 만들어짐
# 실제 비동기식 에러가 발생한 곳의 stack trace를 포함함
d.errback("Triggering errback.")
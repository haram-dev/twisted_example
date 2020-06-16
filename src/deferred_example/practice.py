# -*- coding: utf-8 -*-
from twisted.internet.defer import Deferred


def callback1(result):
    print "Callback 1 said: ", result
    return result


def callback2(result):
    print "Callback 2 said: ", result


def callback3(result):
    raise Exception("Callback 3")


def errback1(failure):
    print "Errback 1 had an error on", failure
    return failure


def errback2(failure):
    raise Exception("Errback 2")


def errback3(failure):
    print "Errback 3 took care of", failure
    return "Everything is fine now."

'''
# example 1
d = Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.callback("Test")
'''

'''
# example 2
d = Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.addCallback(callback3)
# callback3에서 발생하는 예외를 처리할 에러백이 등록되지 않았으므로 프로그램이 종료됨 (Unhandled Error 발생)
d.callback("Test")
'''

'''
# example 3
d = Deferred()
d.addCallback(callback1)
d.addCallback(callback2)
d.addCallback(callback3)
# errback3가 callback3에서 발생한 예외를 처리
d.addErrback(errback3)
d.callback("Test")
'''

'''
# example 4
d = Deferred()
d.addErrback(errback1)
# 에러백 체인을 점화
# 에러백의 첫 번째 매개변수는 항상 실패 객체(Failure)
# 전달된 매개변수는 필요하다면 실패 객체로 wrapping 됨 (아래 코드에서는 문자열 'Test'가 wrapping 됨)
# errback1은 실패를 반환하지만, 해당 실패를 처리할 추가적인 에러백이 없으므로 Unhandled Error 발생
# TypeError: Strings are not supported by Failure 에러 발생 ***
d.errback("Test")
'''

'''
# example 5
d = Deferred()
d.addErrback(errback1)
d.addErrback(errback2)
d.errback("Test")
'''

# example 6
d = Deferred()
d.addErrback(errback2)
d.errback("Test")

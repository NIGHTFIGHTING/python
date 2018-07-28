#-*- encoding: utf8 -*-

def foo():
    print('ok')
    count = yield 1
    print('yes')
    print(count)
    yield 2

b = foo()
s = b.send(None)
print(s)
s = b.send("ee")
print(s)

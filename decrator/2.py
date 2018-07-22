#-*- encoding:utf8 -*-


import time

#装饰器函数
def show_time1(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('show spend1: %s'%(end-start))
    return inner

@show_time1
def foo():
    print('foo ...')
    time.sleep(1)

start = time.time()
foo()
end = time.time()

print(start)
print(end)
print('spend: %s'%(end-start))

def bar():
    print('bar ...')
    time.sleep(3)

def show_time(func):
    start = time.time()
    func()
    end = time.time()
    print('show spend: %s'%(end-start))

show_time(foo)
show_time(bar)

print('----------------')

#foo=show_time1(foo)
foo()
bar=show_time1(bar)
#bar()

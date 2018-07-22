#-*- encoding:utf8 -*-


import time

#装饰器函数
def show_time(func):
    def inner(x,y):
        start = time.time()
        func(x,y)
        end = time.time()
        print('show spend1: %s'%(end-start))
    return inner

@show_time
def add(a, b):
    print(a+b)
    time.sleep(1)

add(3,4)

@show_time
def add1(a, b):
    time.sleep(1)
    return (a+b)

print add1(3,5)

def show_time1(func):
    def inner(*x, **y):
        start = time.time()
        sum = func(*x, **y)
        end = time.time()
        print('show spend1: %s'%(end-start))
        return sum
    return inner

#功能函数加上参数
@show_time1
def add2(*a, **b):
    sum = 0
    for i in a:
        sum +=i
    #print(sum)
    time.sleep(1)
    return sum

print add2(1,2,5,7)

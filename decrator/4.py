#-*- encoding:utf8 -*-

import time

#装饰器函数加参数
def logger(flag = 'true'):
    def show_time(func):
        def inner(*x,**y):
            start = time.time()
            func(*x,**y)
            end = time.time()
            print('show spend1: %s'%(end-start))
            if flag == 'true':
                print('日志记录')
        return inner
    return show_time

'''
相当于
1.logger('true)返回show_time
2.执行@show_time
'''
@logger('true')
def add(*a, **b):
    sum = 0
    for i in a:
        sum +=i
    print(sum)
    time.sleep(1)

@logger('false')
def mul(*a, **b):
    sum = 1
    for i in a:
        sum *=i
    print(sum)
    time.sleep(1)


add(3,4,1)
mul(3,4,2)

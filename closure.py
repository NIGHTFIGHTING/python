#-*- coding: utf-8 -*-

def counter(start = 0):
    count = [start]
    def incr():
        count[0] += 1
        return count[0]
    return incr


def counter2(start = 0):
    def incr():
        nonlocal start
        start += 1
        return start
    return incr 


incr = counter(5)
print(incr())
print(incr())
print(incr())

incr = counter2(5)
print(incr())
print(incr())
print(incr())

def line_conf(a, b):
    def line(x):
        return a*x + b
    return line

line1 = line_conf(1, 1)
line2 = line_conf(4, 5)

print(line1(2))
print(line2(2))

def w1(func):
    def inner():
        print("aaa")
        print("bbb")
        return func()
    return inner

@w1
def f1():
    print('f1')

f1()

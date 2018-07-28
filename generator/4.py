# -*- encodinf: utf8 -*-

def fib(num):
    n, before, after = 0, 0, 1
    while(n < num):
        yield before
        before, after = after, before+after
        n = n + 1

g = fib(8)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#-*- coding:utf-8 -*-

def factorial(n):
    result = n
    for i in range(1, n):
        result *= i
    return result

def factorial_rescursion(n):
    if n == 1:
        return 1
    else:
        return n*factorial_rescursion(n-1)

print factorial(5)
print factorial_rescursion(6)



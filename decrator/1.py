#-*- encoding: utf8 -*-


def outer():
    x = 10
    def inner(): #1.inner就是内部函数
        print(x) #2.外部环境的一个变量
    return inner #结论:内部函数inner就是一个闭包

outer()()
f = outer()
f()

'''
闭包=函数块+定义函数时的环境
'''
def outer1(x):
    def inner(): #1.inner就是内部函数
        print(x) #2.外部环境的一个变量
    return inner #结论:内部函数inner就是一个闭包

outer1(2)()
f = outer1(9)
f()

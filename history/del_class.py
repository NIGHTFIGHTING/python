#-*- coding:utf-8 -*-

import sys

#���ü���

class Dog:
    def __del__(self):
        print("-----hahhha---")


dog1 = Dog();

print(sys.getrefcount(dog1))
dog2 = dog1;
print(sys.getrefcount(dog2))

del dog1
print(sys.getrefcount(dog2))
del dog2

print("-------------")

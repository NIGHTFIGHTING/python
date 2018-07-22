#-*- coding: utf-8 -*-

class Cat:

    def __init__(self):
        print("__init__")
        self.name = ""
        self.age = ""
    __init__.__doc__
    'init'

    def __init__(self, new_name, new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        print("__str__")
        return "%s"%(self.name)

    def eat(self):
        print("cat eat fish")
    
    def drink(self):
        print("cat drink cola")

    def print_all(self):
        self.__print_all()
        print("name=%s"%self.name)
    def __print_all(self):
        print("__print_all:%s"%self.name)

tom = Cat("", "")
tom.eat()
tom.drink()

print(tom)
tom.name = "tom"
print(tom)
#tom.__print_add()

print("name=%s"%tom.name)
tom.print_all()

lanmao = Cat("", "")


class Dog:
    def test():
        print("test")




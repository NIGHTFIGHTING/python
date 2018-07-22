class Animal:
    def eat(self):
        print("----eat---")

class Dog(Animal):
    def init(self):
        print("---init---")
    def bark(self):
        print("---bark---")
    

class XiaoTian(Animal):
    def fly(self):
        print("---fly---")
    def bark(self):
        print("---xiaotian bark---")
        #Dog.bark(self)
        super().bark()

class Gou(Dog, XiaoTian):
    def gou(self):
        print("---gou---")

dog = Dog()
dog.eat()
dog.bark()

xiaotian = XiaoTian()
xiaotian.eat()
#xiaotian.bark()

gou = Gou()
gou.eat()
gou.bark()
gou.fly()
gou.gou()

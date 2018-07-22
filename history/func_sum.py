#-*- coding:  utf-8 -*-

def add(a, b):
    print("%d+%d=%d"%(a, b, a+b))

num1 = int(raw_input("num1:"))
num2 = int(raw_input("num2:"))

add(num1, num2)


def get_temperature():
    tempera = 22
    return tempera

def get_temperature_huashi():
    tempera = get_temperature()
    tempera += 3
    return tempera

tempera = get_temperature_huashi()
print tempera

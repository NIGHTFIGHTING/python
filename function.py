#-*- coding: utf-8 -*-

i = 1

def function(i):
    i += 1
    print("kkkk")
    if (i == 5):
        return 
    else:
        function(i)

def function_a():
    print("qqq")

function_a()
function(1)

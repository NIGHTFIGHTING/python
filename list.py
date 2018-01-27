from __future__ import print_function
#-*- coding:utf-8 -*-

#可以存不同数据类型

names = ["asda","adsa","ddd",1,2]

for i in range(0,len(names)):
    print(names[i],end="")
    print(" ",end="")
print("")

#1
names.append("liuqi")

#2
names.insert(0,"liucheng")

for i in names:
    print (i, end="")
print("")
names2 = ["asda","adsa","ddd",1,2]

#3
names3 = names + names2
for i in names3:
    print (i, end="")
print("")

#4
names3.extend(names3)

for i in names3:
    print (i, end="")
print("")

#5
names3.pop()
for i in names3:
    print (i, end="")
print("")

#6只删除第一个
names3.remove("liuqi")
for i in names3:
    print (i, end="")
print("")

#7del
del names3[0]

for i in names3[::1]:
    print (i, end="")
print("")
#8下标，切片

for i in names3[::-1]:
    print (i, end="")
print("")

#9 in, not in

print ("len=%d"% len(names3))
if "oo" not in names3:
    names3.insert(len(names3)+1, "oo")
    print("not in")
for i in names3[::-1]:
    print (i, end="")
print("")

#10 len
for i in range(0,len(names)):
    print(names[i],end="")
    print(" ",end="")
print("")
print(names3)

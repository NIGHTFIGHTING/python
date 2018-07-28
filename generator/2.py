#-*- encoding: utf8 -*-

#s = [x for x in range(10000000)]
s = (x for x in range(3))
#print(s)
#print(s.next())
#print(s.next())
#print(next(s)) #相当于print(s.__next__())
#print(s.next()) StopIteration

'''
生成器是一个可迭代对象(Interable)
节省内存
'''
for i in s:
    print(i)

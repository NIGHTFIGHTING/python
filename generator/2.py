#-*- encoding: utf8 -*-

#s = [x for x in range(10000000)]
s = (x for x in range(10000000))
print(s)
print(s.next())
print(s.next())
print(next(s)) #相当于print(s.__next__())

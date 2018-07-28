# -*- encoding:utf8 -*-

dic=str({'1':'111'})
f = open('test', 'w')
f.write(dic)
f.close()

f= open('test', 'r')
data = f.read()
print(eval(data)['1'])
f.close()

#-*- coding: utf-8 -*-
from __future__ import print_function

infor = {'age':18, 'names': 'aaa'}

#print (infor)
#print infor.get("age")
#print infor.keys()
#if "names" in infor.keys():
    #print infor['names']

#print infor.values()

for i in infor.keys():
    print(i, end=":")
    print(infor[i])


inform = [('age', 18), ('names', 'aaa')]
inform = dict(name='liuqi', age = 124)

d = dict(inform)
print (d)
for i in d.keys():
    print(i, end=":")
    print(d[i])

phonebook = {'Beth':'9102', 'alice':'2341'}
print ("alice's phone number is %(alice)s"%(phonebook))

template = '<html><head><title>%(title)s</title></head><body></body>'
data = {'title': 'MyHomePage'}

print (template % data)

d = {'name': '11'}
if d.get('name') != None:
    print(d['name'])
else:
    print("do'not have d")

if 'name' in d:
    print("in")

#-*- encoding: utf8 -*-

s = set("aaaa bbb")
print(s)

s1 = ["aaa","bbb","aaa"]
s2 = set(s1)
print(s2)
print(s2, type(s2))

# 不可以print(s2[0]),可以通过迭代器
# 无序,不重复
for i in s2:
    print i

s = list(s2)
print(s, type(s))
print("aaa" in s2)
print(2 in s2)

#添加一个元素
s2.add('aa')
print(s2, type(s2))

s2.update('ops')
print(s2, type(s2))

s2.update([12, 'eee'])
print(s2, type(s2))

#删除
s2.remove('aaa')
print(s2, type(s2))

#随机删除
s2.pop()
print(s2, type(s2))
s2.pop()
print(s2, type(s2))

#清空
s2.clear()
print(s2, type(s2))

#删除
del s2

#子集超集
print(set("alex") == set("axelxxxeellaa"))
print(set("alex") < set("axelxxxjjjlaa"))

print(set("alexqqq") and set("bbbaxelxxxeellaa"))
print(set("alex") or set("axelxxxjjjlaa"))

a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])
#交集
print a.intersection(b)
#并集
print a.union(b)

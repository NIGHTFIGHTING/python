import copy

s = [1, 'qq', 'bb']
#s2 = s.copy()
s2 = s[:]
s2[0] = 'aa'

for i in s:
    print i

print s2


s = [[1, 2], 'qq', 'bb']
'''
shallow copy
'''
#s3 = s.copy()
s3 = copy.copy(s)
#s3 = s[:]
print(s3)
s3[0][0] = 3
print(s3)
print(s)

s4 = copy.deepcopy(s)
s4[0][0]='aaa'
print s4
print(s)

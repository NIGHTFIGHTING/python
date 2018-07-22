
a = "liu"
b = "qi"

print a+b
print len(a+b)
print "++++" + a + "---"

f = "++++%s===="%(a+b)
print f

for i in range(0,len(f)):
    print f[i]
    i += 1

print f[2:-2]
print f[2:]
print f[2:-1:2]
print f[-1:0:-1]
print f[-1::-1]
print f[::-1]
print f[::1]

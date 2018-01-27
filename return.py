
def test():
    a = 2
    b = 3
    c = 4
    d = [a, b, c]
    e = {}
    e["aa"] = d
    return (e, a, b , c)

jieguo = test()
print jieguo
for i in jieguo:
    print i

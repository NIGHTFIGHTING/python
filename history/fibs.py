
def fibs(num):
    result = [0, 1]
    for i in range(num-2):
        result.append(result[-2] + result[-1])
    return result

fibs.__doc__
'Calculates th square of the number x'

num = int(raw_input("please input number:"))

result = fibs(num)
print(result)

lables = ('first', 'middle', 'last')
lables = 'first', 'middle', 'last'
print(lables)

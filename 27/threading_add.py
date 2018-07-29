# -*- encoding:utf8 -*-

import time
import threading

begin = time.time()

def add(n):
    time.sleep(3)
#    sum = 0
#    for i in range(n):
#        sum += i
#        i += 1
#    print(sum)

#add(10000000)
#add(20000000)

t1 = threading.Thread(target = add, args = (10000000,))
t1.start()

t2 = threading.Thread(target = add, args = (20000000,))
t2.start()

t1.join()
t2.join()

end = time.time()
print(end-begin)

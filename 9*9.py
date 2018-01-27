from __future__ import print_function
#-*- coding:utf-8 -*-

i = 1;

while i <= 9:
    j = 1;
    while j <= i:
        print("%d * %d = %d\t"%(i, j,int(i*j)), end="")
        j+=1;
    print("")
    i+=1;

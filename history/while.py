from __future__ import print_function

num = 1

num += 0

while num <= 5:
    #print num;
    line = int(raw_input("please input line:"))
    j = 1
    while j <= line:
        print("*", end="")
        j += 1 
    print("");
    num += 1

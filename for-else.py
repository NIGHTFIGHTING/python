from __future__ import print_function
card_infos = [{"name":"asda","age":18,"tt":{"asda":00}},{"name":"999","ppp":11},{"111":111}]

#find_name = raw_input("please input name:")

for i in card_infos:
    print (i.keys())
    for j in i.keys():
        print("key:%s"%j, end=" values:")
        print(i[j])
    #if i['name'] == find_name:
     #   print("good")
      #  break
    
#else:
    #print("do'not find")

print ("------------")


for i in card_infos:
    print (i.items())
    for j in i.items():
        print("key=%s, value=%s"%(j[0], j[1]))
print ("------------")
for i in card_infos:
    print (i.items())
    #for j in i.items():
        #key,value = j
    for key,value in i.items():
        print("key=%s, value=%s"%(key, value))

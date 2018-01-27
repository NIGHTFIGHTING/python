from __future__ import print_function

#import json


card_infos = '{"name":"asda","age":18,"tt":{"asda":00}}'

#dictinfo = json.loads(card_infos)
dict_card_infos = eval(card_infos)

print("card_infos: %s"%card_infos)
for key,value in eval(card_infos).items():
    print("key=", key, " value=", value)
 

print(dict_card_infos)
print("dict_card_infors: %s"%dict_card_infos)
for key,value in dict_card_infos.items():
    print("key=", key, " value=", value)

str_card_infos = str(dict_card_infos)
print("str_card_infors: %s"%str_card_infos)

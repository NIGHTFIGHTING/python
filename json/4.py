import json

dict = {'name' : 'alex', 'age' : '18'}
f = open('JSON_text', 'w')
data = json.dump(dict, f)
f.close()

f = open('JSON_text', 'r')
data = json.load(f)
print(data)
print(data['name'])

import json

dict = {'name' : 'alex', 'age' : '18'}

data = json.dumps(dict)
print(data)
f = open('JSON_text', 'w')
f.write(data)
f.close()


f = open('JSON_text', 'r')
#data = json.load(f)
data = f.read()
data = json.loads(data)
print(data['name'])
f.close()

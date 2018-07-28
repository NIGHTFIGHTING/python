import pickle

def foo():
    print('ok')



data = pickle.dumps(foo)
print(data)
f = open('JSON_text', 'wb')
f.write(data)
f.close()


f = open('JSON_text', 'r')
#data = json.load(f)
data = f.read()
data = pickle.loads(data)
print(data)
data()
f.close()

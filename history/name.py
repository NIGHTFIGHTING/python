#-*- coding: utf-8 -*-
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data, label, name):
    #return data[label].get(name)
    return data.get(label).get(name)

def store(data, full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1, '')
    labels = ('first', 'middle', 'last')
    print (labels)
    print (names)
    print (zip(labels, names))
    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


def store_all(data, *full_names):
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2:
            names.insert(1, '')
        labels = ('first', 'middle', 'last')
        print (labels)
        print (names)
        print (zip(labels, names))
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]
MyNames = {}
init(MyNames)
print(MyNames)

store(MyNames, "Liu Qi")
store(MyNames, "Ying Qi")
store(MyNames, "Liu Da Cheng")
store_all(MyNames, "Liu haha Cheng", "Liu 66 Cheng")
print(MyNames)
print ("------------------")
print "first Liu:", lookup(MyNames, 'first', "Liu")
print "middle Da:", lookup(MyNames, 'middle', "Da")
print "last Cheng:", lookup(MyNames, 'last', "Cheng")
print "last Qi:", lookup(MyNames, 'last', "Qi")

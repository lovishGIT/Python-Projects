import json
d= {
    'a': 12,
    'b': [1,2,3,4,5],
    'c': "hello",
}

with open("ten.json", 'w') as file:
    json.dump(d, file)

# d['a']

a= json.dumps(d)

print(a)
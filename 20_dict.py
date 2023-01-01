#Dictionaries

person = {
    'name': 'Rene',
    'last_name': 'Mejia',
    'langs': ['PHP', 'Python'],
    'age': 33
}

print(person)
person['name'] = 'Not Rene'
person['age'] +=10
person['langs'].append('Ruby')
person['status'] = 'married'

print(person)

del person['last_name'] #delete
person.pop('age') #Also delete
print(person)

print('items')
print(person.items())

print('keys')
print(person.keys())

print('values')
print(person.values())
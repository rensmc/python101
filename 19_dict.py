#Dictionaries

my_dict = {}
print(type(my_dict))

my_dict = {
    'avion': 'bla bla bla',
    'name': 'Rene',
    'last_name': 'Mejia',
    'age': 33
}

print(my_dict)
print(len(my_dict))

print(my_dict['name'])
print(my_dict['last_name'])
print(my_dict['age'])
print(my_dict.get('age')) 

value = my_dict.get('some_value') #With get you can handle errors.
print(value)

print('avion' in my_dict)
print('notavalue' in my_dict)

#for loop

'''
for element in range(1, 21): #Starts from 1, ends in 20.
    print(element)
'''

my_list = [23, 45, 67, 89, 43]
for i in my_list:
    print(i)

my_tuple = ('nico', 'juli', 'santi')
for i in my_tuple:
    print(i)

#============================


product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89
}

for i in product:
    print(i, '=>', product[i])

for key, value in product.items():
    print(key, '=>', value)

#============================

people = [
    {
        'name': 'nico',
        'age': 34,
    },
    {
        'name': 'sule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 4
    }
]

for person in people:
    print(person)
#Tupla/Tuple - Estructura de datos inmutables que contiene una secuencia ordenada de elementos.

numbers = (1, 2, 3, 5)
strings = ('nico', 'zule', 'santi', 'nico')
print(numbers)
print('0 => ', numbers[0])
print('-1 => ', numbers[-1])
print(type(numbers))

print(strings)
print(type(strings))

#CRUD
#numbers.append(10) #Error: Object cannot be modified.
#print(numbers)
#numbers[1] = 'change' #Error: Object cannot be modified.

print(strings)
print(strings.index('zule'))
print(strings.count('nico'))

my_list = list(strings)
print(type(my_list)) #The only way tu modify a tuple is transforming it into a list.

my_list[1] = 'juli'
print(my_list)

my_tuple = tuple(my_list)
print(my_tuple)
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))

tasks = ['Make dishes', 'Play videogames'] #A list of strings.
print(tasks)
print(tasks[1])

types = [1, True, 'hola'] #You an create lists with different types of data.
print(types)

print(numbers[0])
print(tasks[0])

text = 'Hola'
#text[0] ='W' #Error: String object does not support item assignment.

tasks[0] = 'Read a book'
print(tasks)

print(numbers[:3])
print(True in types)
print('Hola' in types)
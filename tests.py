
name = input('¿Cuál es tu nombre? => ')
print(name)
last_name = input('¿Cuál es tu apellido? => ')
print(last_name)
age = input('¿Cuál es tu edad? => ')
print(age)
age = int(age)
ageFuture = age + 10

template = f"Hola mi nombre es {name} {last_name}, tengo {age} años y en 10 años tendré {ageFuture} años"
print(template)
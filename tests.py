
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


#Determinar si un número es par o impar

numero = int(input("Digita un número y te diré si es par o impar => "))
if numero % 2 == 0:
    print(f"{numero} es un número par")
else:
    print(f"{numero} no es un número par")
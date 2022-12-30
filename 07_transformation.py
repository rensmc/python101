#https://platzi.com/clases/4227-python/54992-transformacion-de-tipos/

#String
name = "Rene"
print(type(name))

#Int
name = 12
print(type(name))

#Boolean
name = True
print(type(name))

print("Rene " + "Mejia")
print(10 + 20)
#Error: print("Rene" + 10)

#Transformar a string para concatenar
age = 12
print("Mi edad es " + str(age))
print(f"Mi edad es {age}")

#Input
age = input("Escribe tu edad => ")
age = int(age)
age += 10
print(f"Tu edad en 10 años será {age}")

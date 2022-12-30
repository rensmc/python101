x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

print(x == y) #No son iguales debido a la cantidad de decimales en y

#Comparar en forma de strings
y_str = format(y, ".2g")
print("str => ", y_str)
print(y_str == str(x))

print("-" * 20) #---------------------

#Comparar matemáticamente
print(x, y)
tolerance = 0.00001
print(abs(x -y) < tolerance)

print("-" * 20) #---------------------

#comparar redondeando números
print(x == round(y,1))
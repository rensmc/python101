print(not True)
print(not False)

# and
print("NOT AND")
print("True and True =>", not (True and True)) #False
print("True and False =>", not (True and False)) #True
print("False and True =>", not (False and True)) #True
print("False and False =>", not (False and False)) #True

print("-" * 20)

stock = int(input("Ingrese el número de stock => "))
print(not (stock >= 100 and stock <= 1000))

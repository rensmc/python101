name = "Rene"
last_name = "Mejia"
print(name)
print(last_name)

# Concat
full_name = name + " " + last_name
print(full_name)

#Errores con apostofe
#quote = 'I'm Rene'
#quote2 = ""She said hello...""

#Correcciones
quote = "I'm Rene"
quote2 = 'She said "hello..."'
print(quote2)

#Format
template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print("v1", template)

template = "Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print("v2", template)

template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print("v3", template)
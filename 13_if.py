# if

if True:
    print("Debería ejecutarse")

if False:
    print("Esto no debería ejecutarse")


pet = input("Cuál es tu mascota favorita? => ")

if pet == "perro":
    print("Genial! yo también amo a los perritos")

if pet == "gato":
    print("Espero tengas suerte...")
    

# if / else

stock = int(input("Digita el stock => "))

if stock >= 100 and stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock no es correcto")


# elif = al cumplir una de las condiciones, automáticamente descarta las demás. Optimiza el procesamiento.

pet = input("Cuál es tu mascota favorita? => ")

if pet == "perro":
    print("Genial! yo también amo a los perritos")
elif pet == "gato":
    print("Espero tengas suerte...")
elif pet == "pez":
    print("Eres lo máximo")
else:
    print("Tu mascota no es interesante")
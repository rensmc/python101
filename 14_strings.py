#Operador in - Busca el texto que le indiquemos en la cadena de caracteres.

text = 'Ella sabe programar en Python'
print('JavaScript' in text)
print('Python' in text)

if 'Python' in text:
    print('Muy bien!')
else:
    print('Muy bien también!')

#len() - Tamaño de las cadenas de caracteres

size = len('amor')
print(size)

#upper() - convertir todo a mayúsculas.
#lower() - convertir todo a minúsculas.
#count() - Contar el número de veces que se presenta el texto que le indiquemos en la cadena de caracteres.
#swapcase() - Invertir el capitalizado de todos los caracteres en una cadena.
#startswith() - consultar si la cadena de caracteres inicia con el texto que le indiquemos. Booleano.
#endswith() - consultar si la cadena de caracteres finaliza con el texto que le indiquemos. Booleano.
#replace() - Reemplaza un texto por el que nosotros indiquemos.
#capitalize() - Capitaliza la primer letra de un texto.
#title() - Capitaliza la primer letra de cada palabra del texto.
#isdigit() - consulta si la cadena de caracteres es un número.

print(text)
print(text.upper())
print(text.lower())
print(text.count('a'))

print(text.swapcase())
print(text.startswith('Ella'))
print(text.endswith('Ella'))
print(text.replace('Python', 'Go'))

text_2 = 'este es un titulo'
print(text_2.capitalize())
print(text_2.title())
print(text_2.isdigit())
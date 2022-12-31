#Indexing

text = "Ella sabe Python"
print(text[0])
print(text[1])

#print(text[999]) #Error: String index out of range.

#Cómo determinar la posición final de un texto?

size = len(text)
print('size => ', size)
#print(text[size]) #Error: String indez out of range. Las posiciones comienzan desde 0, no 1. 
# Así que la última posición es 15, no 16.

print(text[size - 1]) #Correcto.
print(text[-1]) #Also, last character of a string.
print(text[-2]) #Second to last character of a string.

#positions in a string
# 0  1  2  3  4  5  6 - Forward
#-7 -6 -5 -4 -3 -2 -1 - Backward

#Slicing

print(text[0:5])
print(text[10:16])
print(text[:10]) #From position 0 to 10.

print(text[5:-1]) #Error: skips last character.
print(text[5:]) # Correction: From position 5 to last character

#Other examples of slicing.

print(text[:]) #Ella sabe Python
print(text[10:16:1]) #Python
print(text[10:16:2]) #Pto
print(text[::2]) #El aePto
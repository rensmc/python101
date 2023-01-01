#While loop


''' Example: Endless loop
while True:
    print('Se ejecutó') 

'''

print('Example: Adding a clause')
counter = 0
while counter < 10:
    counter += 1
    print(counter)
print('-' * 25)

print('Example: Breaking the loop.')
counter = 0
while counter < 20:
    counter += 1
    if counter == 15: 
        break
    print(counter)
print('-' * 25)

print('Example: Jump in the loop')
counter = 0
while counter < 20:
    counter += 1
    if counter < 15:
        continue
    print(counter)
print('-' * 25)
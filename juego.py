# Juego de piedra, papel o tijera

import random

options = ['piedra', 'papel', 'tijera']
computer_option = random.choice(options)

user_option = input('Juguemos! Elige piedra, papel o tijera => ')
user_option = user_option.lower()

if user_option == computer_option:
    print(f"La computadora ha elegido {computer_option}")
    print("Es un empate")

elif user_option == 'piedra':
    if computer_option == 'tijera':
        print(f'La computadora eligió {computer_option}')
        print('Piedra gana a tijera')
        print('Has ganado!')
    else:
        print(f'La computadora ha elegido {computer_option}')
        print('Papel gana a piedra')
        print('La computadora ha ganado')

elif user_option == 'papel':
    if computer_option == 'piedra':
        print(f'La computadora eligió {computer_option}')
        print('Papel gana a piedra')
        print('Has ganado!')
    else:
        print(f'La computadora eligió {computer_option}')
        print('Tijera gana a papel')
        print('La computadora ha ganado')

elif user_option == 'tijera':
    if computer_option == 'piedra':
        print(f'La computadora eligió {computer_option}')
        print('Piedra gana a tijera')
        print('La computadora ha ganado')
    else:
        print(f'La computadora eligió {computer_option}')
        print('Tijera gana a papel')
        print('Has ganado!')

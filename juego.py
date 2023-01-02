# Juego de piedra, papel o tijera

import random

options = ('piedra', 'papel', 'tijera')

rounds = 1
user_wins = 0
computer_wins = 0

while True:

    print('-' *20)
    print('Round => ', rounds)
    print('-' *20)

    computer_option = random.choice(options)

    user_option = input('Juguemos! Elige piedra, papel o tijera => ')
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
        print('Esa opción no es válida 🚫')

    if user_option == computer_option:
        print(f"Tu rival ha elegido {computer_option}")
        print("Es un empate 😬")
        print('Rival: ', computer_wins, 'pts', ' - Tú ', user_wins, 'pts')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print(f'Tu rival eligió {computer_option}')
            print('Piedra gana a tijera')
            print('Has ganado! 🎉')
            print('Rival: ', computer_wins, 'pts', ' - Tú ', user_wins, 'pts')
            user_wins += 1
        else:
            print(f'Tu rival ha elegido {computer_option}')
            print('Papel gana a piedra')
            print('Tu rival ha ganado 🫠')
            print('Rival: ', computer_wins, 'pts', ' - Tú ', user_wins, 'pts')
            computer_wins += 1

    elif user_option == 'papel':
        if computer_option == 'piedra':
            print(f'Tu rival eligió {computer_option}')
            print('Papel gana a piedra')
            print('Has ganado! 🎉')
            print('Rival: ', computer_wins, 'pts', ' - Tú ', user_wins, 'pts')
            user_wins += 1
        else:
            print(f'Tu rival eligió {computer_option}')
            print('Tijera gana a papel')
            print('Tu rival ha ganado 🫠')
            print('Rival: ', computer_wins, 'pts', ' - Tú ', user_wins, 'pts')
            computer_wins += 1

    elif user_option == 'tijera':
        if computer_option == 'piedra':
            print(f'Tu rival eligió {computer_option}')
            print('Piedra gana a tijera')
            print('Tu rival ha ganado 🫠')
            print('Rival: ', computer_wins, 'pts', ' - Tú ', user_wins, 'pts')
            computer_wins += 1
        else:
            print(f'Tu rival eligió {computer_option}')
            print('Tijera gana a papel')
            print('Has ganado! 🎉')
            print('Rival: ', computer_wins, 'pts', ' - Tú ', user_wins, 'pts')
            user_wins += 1
    
    if computer_wins == 3:
        print('-' *20)
        print('Has perdido la partida 😥')
        print('Rival: ', computer_wins, ' pts', ' - Tú ', user_wins, ' pts')
        break

    if user_wins == 3:
        print('-' *20)
        print('Felicidades! Has ganado la partida! 🏆')
        print('Rival: ', computer_wins, ' pts', ' - Tú ', user_wins, ' pts')
        break

    

import os
import funciones


clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')


while True:
    print('''
    +------------------------------------------+
    |            ANALIZADOR DE EMAIL           |
    +------------------------------------------+

Ingrese una dirección de correo electrónico o ingrese [X] para salir.
    ''')
    email = input().lower().replace(' ', '')
    clearConsole()

    if email.upper() == 'X':
        exit()
    elif funciones.comprobar_email(email) == False:
        print('ERROR: ingrese un email válido.')
        continue
    else:
        funciones.analizar_email(email)

    ENTER = input('[ENTER] Inicio')
    clearConsole()
# user should type an int, in which case, it will be returned by this function
# otherwise user stays on loop until typing 'q'

import sys


def enteroOrQuit():
    valor = ''
    while valor != 'q':
        print('\n','\n', 'escribe un entero, o "q" para terminar...', '\n', '-->', end='')
        valor = input()
        if valor == 'q':
            print('adios...')
            sys.exit()
        else:
            try:
                valor = int(valor)
                return valor
            except ValueError:
                print('no seguiste instruccciones... escribe un entero...')




if __name__ == '__main__':
    enteroOrQuit()

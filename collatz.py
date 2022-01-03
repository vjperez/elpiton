# the output is the collatz sequence for the integer entered by the user

import enteroOrQuit, printeaSeq


valor = enteroOrQuit.enteroOrQuit()

if valor > 0:
    lista = []
    lista.append(valor)

    while valor != 1:
        if valor % 2 == 0:
            valor = valor // 2
        else:
            valor = 1 + 3 * valor

        lista.append(valor)

    printeaSeq.printeaSeq('secuencia collatz', lista)
else:
    print('aqui solo bregamos con enteros mayores q cero...')

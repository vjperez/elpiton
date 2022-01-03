# user should type one of the values on the seq which is argument to this function, 
# in which case, it will be returned by this function
# otherwise user stays on loop until typing 'q'


import sys, printeaSeq


def onSequenceOrQuit(seq):
    valor = ''
    while valor != 'q':
        printeaSeq.printeaSeq('\n\nlas opciones', seq)
        print('escribe uno de esos valores de arriba, o "q" para terminar...', '\n', '-->', end='')
        valor = input()
        if valor == 'q':
            print('adios...')
            sys.exit()
        else:
            if valor in seq:
                return valor
            else:
                print('no seguiste instruccciones...')
                printeaSeq.printeaSeq('las opciones', seq)
                print(valor, 'no esta en las opciones de arriba...')




if __name__ == '__main__':
    # to work with numbers as opciones.... some extra code is needed.       try: int(valor) ?!
    # a= [2, 'victor', 4, 8]
    # onSequenceOrQuit(a)

    # all opciones are str
    a= ['2', 'victor', '4', '8']
    onSequenceOrQuit(a)

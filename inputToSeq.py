# accept input strings and place them on list 
# user can end loop using 'ya'

lista = []
print('Escribe lineas terminadas por RETURN.\nCONTROL + C causa Keyboard Interrupt, y detiene los input.\n\n')

sigo = True
while(sigo):
    try:
        str = input('Input str: ')
        lista.append(str)
    except(KeyboardInterrupt):
        sigo = False
        print('\n\n')



# entered string are re printed in reverse
if __name__ == '__main__':

    import printeaSeq

    printeaSeq.printeaSeq('lista', lista)
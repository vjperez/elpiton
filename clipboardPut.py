#!/usr/bin/python

# Putting a particular message on the clipbooard
# Puts on the clipboard one of values on the mensajes dict
# The keys are used to select which value is stored on the clipboard

import pyperclip, sys

mensajes = {'hola':'Saludos, todo bien?', 
             'ask':'Tiene un minuto disponible?.  Tengo una pregunta.',
             'repo':'https://github.com/asweigart/zombiedice.git' }

# print (sys.argv)     just wanted to see it !
if len(sys.argv) < 2:
    print('You need an argument after the script name, to select a message to copy to the clipboard.')
    print('Available message keys are:', mensajes.keys(), '\nIn other words:', list(mensajes.keys()))
    sys.exit()
elif len(sys.argv) > 2:
    key = sys.argv[1]
    print('You used more arguments than needed, using only arg=', key)
else:
    key = sys.argv[1]


if key in mensajes.keys():
    elMensaje = mensajes[key]
    pyperclip.copy(elMensaje)
    print('Copied to clipboard:', elMensaje)
else:
    print(key, ' was not found as one of the keys.')
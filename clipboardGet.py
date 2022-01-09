#!/usr/bin/python

# Gets the text stored on the clipboard and stores it on the 
# variable below


import pyperclip

textOnClipboard =  pyperclip.paste()

if __name__ == '__main__':
    print('Este es el texto del clipboard:', textOnClipboard)
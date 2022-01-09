#!/usr/bin/python

# textOnClipboard must contain the repo address after calling
# pyperclip.paste().  You copy this string from github...
# for example  ...  https://github.com/asweigart/zombiedice.git


import pyperclip, os

textOnClipboard =  pyperclip.paste()
command = 'git clone ' + textOnClipboard
os.system( command )
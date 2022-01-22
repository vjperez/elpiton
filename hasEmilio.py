import re 

def hasEmilio(str):
    phoneNumberReObj = re.compile(r'''(


 	
r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


    (   (\d{3})   |   (\(\d{3}\))   )   #area code with or without ()
    
    (- | \s | \.)                       #separator  es:  - .  o espacio
    (\d{3})
    (- | \s | \.)                       #separator  es:  - .  o espacio
    (\d{4})
    )''', re.VERBOSE)
        
    matchObject = phoneNumberReObj.search(str)
    #print('\n\n', matchObject)
    if matchObject == None: 
        return False
    else: 
        return matchObject.group()



if __name__ == '__main__':
    
    text = 'aqui no'
    ph = hasPhonenumber(text)
    print('text=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found')   

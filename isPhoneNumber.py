import re

def hasPhonenumber(str):
    phoneNumberReObj = re.compile(r'''(

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

    text = 'jhffgh787-234-2323jhgf'
    ph = hasPhonenumber(text)
    print('\ntext=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found') 

    text = 'kjg (939)-233-447744oiyu'
    ph = hasPhonenumber(text)
    print('\ntext=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found') 
    
    text = 'kjh*()939-233-4444gfds'
    ph = hasPhonenumber(text)
    print('\ntext=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found') 

    text = 'rewq939)-233-4444;lj'
    ph = hasPhonenumber(text)
    print('\ntext=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found') 

    text = '939(-233-4444'
    ph = hasPhonenumber(text)
    print('\ntext=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found') 

    text = 'rewq(939).233.4444;lj'
    ph = hasPhonenumber(text)
    print('\ntext=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found') 

    text = 'rewq(787) 233 4444;lj'
    ph = hasPhonenumber(text)
    print('\ntext=', text, 'ph=', ph)
    if ph:  print(ph)
    else:   print('no phone number found') 
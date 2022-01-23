import re 

def hasEmilio(str):
    # re implemented below with ''' and re.VERBOSE
    # r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    # re is not perfect but should get some emails
    emilioReObj = re.compile( r'''(
        [a-zA-Z0-9_.+-]+
        @
        [a-zA-Z0-9-]+
        \.
        [a-zA-Z0-9-.]+
    )''' ,re.VERBOSE)

        
    matchObject = emilioReObj.search(str)
    print('\n\nmatch object= ', matchObject)
    if matchObject == None: 
        return False
    else: 
        return matchObject.group()



if __name__ == '__main__':
    
    text = 'aqui no'
    emilio = hasEmilio(text)
    print('text=', text, '\nemilio=', emilio)
    if emilio:  
        print(emilio)
    else:   
        print('no emilio found')  


    text = 'wer vd@rf.com lkjh'
    emilio = hasEmilio(text)
    print('text=', text, '\nemilio=', emilio)
    if emilio:  
        print(emilio)
    else:   
        print('no emilio found')   


    text = 'wer cosa-co3sa@cosa-cosa.com-com lkjh'
    emilio = hasEmilio(text)
    print('text=', text, '\nemilio=', emilio)
    if emilio:  
        print(emilio)
    else:   
        print('no emilio found') 


    text = 'wer cosa-co3sa@co.sa-cosa.com-co.m lkjh'
    emilio = hasEmilio(text)
    print('text=', text, '\nemilio=', emilio)
    if emilio:  
        print(emilio)
    else:   
        print('no emilio found') 
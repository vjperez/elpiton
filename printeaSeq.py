# name will appear at the left of the :
# items on the seq will appear to the right of :

def printeaSeq(name, seq):
    if isinstance(name, str):  #should also check, seq is a collection ?!
        print(name, ': ', sep='', end='') 
        for item in seq:
            print(item, ' ', sep='', end='')
        print('', end='\n')
    else:
        raise Exception('Primer arg no es string...')


if __name__ == '__main__':

    a= []
    printeaSeq('vacio', a)

    a= ["victor"]
    printeaSeq('mi nombre', a)

    a= [2, 'victor']
    printeaSeq('2 y mi nombre', a)

    #aqui 23 no es un str... raising an exception...
    a= [4, 7]
    printeaSeq(23, a)
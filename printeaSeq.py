# name will appear at the left of the =
# items on the seq will appear to the right of =

def printeaSeq(name, seq):
    print(name, '= ', sep='', end='') 
    for item in seq:
        print(item, ' ', sep='', end='')
    print('', end='\n')


if __name__ == '__main__':

    a= []
    printeaSeq('vacio', a)

    a= ["victor"]
    printeaSeq('mi nombre', a)

    a= [2, 'victor']
    printeaSeq('2 y mi nombre', a)
# conway game of life
# simulation will run on l X l spots
# beings will be randomly created initially
# then they will evolve using 
# evolve.py

import enteroOrQuit, random

def zeroOrOne():
    return random.randint(0,1 )


def getConwayInitWorld():
    space = []
    l = enteroOrQuit.enteroOrQuit()
    for a in range(l):
        row = []
        for b in range(l):
            n = zeroOrOne()
            if n == 0:
                row.append(' ')
            else:
                row.append('#')
        space.append(row)
    return [space, l]




if __name__ == '__main__':
    print (getConwayInitWorld())
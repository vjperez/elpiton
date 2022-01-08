import getIniSpace, copy

def printWorld(s):
    for row in s:
        for item in row:
            print(item,  end='')
        print('', end='\n')
    print('\n\n\n')


def emptyWorld(world):
    for row in world:
        for item in row:
            if isCellAlive(item):    return False
    return True


def fullWorld(world):
    for row in world:
        for item in row:
            if not isCellAlive(item):    return False
    return True


def stableWorld(world, size, newWorld):
    for x in range(size):
        for y in range(size):
            if world[x][y] != newWorld[x][y]:    return False
    return True


def isCellAlive(item):
    return item == '#'


def willCellSurvive(world, size, r, c):
    if howManyNeibhors(world, size, r, c) >= 3: return True
    else:   return False


def shouldCreateCell(world, size, r, c):
    if howManyNeibhors(world, size, r, c) >= 2: return True
    else: return False


def howManyNeibhors(world, size, r, c):
    n = 0 # no neighbors
    # looking for neibohors, spots at the edge connect with opposite edge
    if isCellAlive( world[r][(c+1)%size] ): n += 1
    if isCellAlive( world[(r+1)%size][c] ): n += 1
    if isCellAlive( world[r][(c-1+size)%size] ): n += 1
    if isCellAlive( world[(r-1+size)%size][c] ): n += 1
    # diagonal neighbors
    if isCellAlive( world[(r+1)%size][(c+1)%size] ): n += 1
    if isCellAlive( world[(r+1)%size][(c-1+size)%size] ): n += 1
    if isCellAlive( world[(r-1+size)%size][(c+1)%size] ): n += 1
    if isCellAlive( world[(r-1+size)%size][(c-1%size)%size] ): n += 1
    # print('r', r, 'c', c, 'n', n)
    return n


def aNewWorld(world, newWorld, size):
    for r, row in enumerate (world):
        for c, item in enumerate (row):
            if isCellAlive(item):
                if willCellSurvive(world, size, r, c):
                    pass
                    # cell is there and will survive
                else:
                    newWorld[r][c] = ' '
            else: # no cell in this spot, so should i create one ?
                if shouldCreateCell(world, size, r, c):
                    newWorld[r][c] = '#'
                else:
                    pass
                    # no cell there, and no cell will be created


worldAndSize = getIniSpace.getIniSpace()
size  = worldAndSize[1]
world = worldAndSize[0]


newWorld = copy.deepcopy(world)
aNewWorld(world, newWorld, size)
iteration = 1
print('Creation:')
printWorld(world)
print('First new world, before loop iterations:')
printWorld(newWorld)
input()

while not stableWorld(world, size, newWorld):
    world = copy.deepcopy(newWorld)
    aNewWorld(world, newWorld, size)
    iteration += 1
    print('Iteration', iteration)
    printWorld(newWorld)
    input()


print('\n\nIteration:', iteration, 'produced the same world.')

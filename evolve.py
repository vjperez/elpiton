import getIniSpace, copy


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


def stableWorld(worldAndSize, newWorld):
    size  = worldAndSize[1]
    world = worldAndSize[0]
    for x in range(size):
        for y in range(size):
            if world[x][y] != newWorld[x][y]:    return False
    return True


def isCellAlive(item):
    return item == '#'


def willCellSurvive(worldAndSize, r, c):
    if howManyNeibhors(worldAndSize, r, c) >= 1: return True
    else:   return False


def shouldCreateCell(worldAndSize, r, c):
    if howManyNeibhors(worldAndSize, r, c) >= 1: return True
    else: return False


def howManyNeibhors(worldAndSize, r, c):
    size  = worldAndSize[1]
    world = worldAndSize[0]
    n = 0 # no neighbors
    # looking for neibohors, spots at the edge connect with opposite edge
    if isCellAlive( world[r][(c+1)%size] ): n += 1
    if isCellAlive( world[(r+1)%size][c] ): n += 1
    if isCellAlive( world[r][(c-1+size)%size] ): n += 1
    if isCellAlive( world[(r-1+size)%size][c] ): n += 1
    print('r: ', r, 'c: ', c, 'n: ', n)
    return n



worldAndSize = getIniSpace.getIniSpace()
size  = worldAndSize[1]
world = worldAndSize[0]
print('\n\nCreation:\nworld    ', world, '\n\n')
newWorld = copy.deepcopy(world)


iteration = 0
isStableWorld = False
while not isStableWorld:
    for r, row in enumerate (world):
        for c, item in enumerate (row):
            if isCellAlive(item):
                if willCellSurvive(worldAndSize, r, c):
                    pass
                    # cell is there and will survive
                else:
                    newWorld[r][c] = ' '
            else: # no cell in this spot, so should i create one ?
                if shouldCreateCell(worldAndSize, r, c):
                    newWorld[r][c] = '#'
                else:
                    pass
                    # no cell there, and no cell will be created
    print('After iteration ', iteration, ':\nworld    ', world)
    print('new world', newWorld, '\n\n\n\n')
    input()

    isStableWorld = stableWorld(worldAndSize, newWorld)

    iteration += 1
    world = copy.deepcopy(newWorld)
    worldAndSize = [newWorld, size]
print('\n\nStable world beginning iteration:', iteration, '. Iteration', iteration - 1, 'created a stable world.')

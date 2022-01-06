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


def isCellAlive(item):
    return item == '#'


def willCellSurvive(worldAndSize, r, c):
    if howManyNeibhors(worldAndSize, r, c) >= 2: return True
    else:   return False


def shouldCreateCell(worldAndSize, r, c):
    if howManyNeibhors(worldAndSize, r, c) >= 3: return True
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
while not emptyWorld( newWorld ) and not fullWorld( newWorld ):
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
    print('Iteration ', iteration, ':\nworld    ', world)
    print('new world', newWorld, '\n\n\n\n')
    input()

    iteration += 1
    world = copy.deepcopy(newWorld)
    worldAndSize = [newWorld, size]
print('\n\nEmpty, full or ===stable=== world beginning iteration:', iteration, '. Iteration', iteration - 1, 'killed everyone.')

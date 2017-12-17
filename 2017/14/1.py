import math
from binascii import unhexlify

def reverseRange(collection, start, end):

    nbOfSwaps = int(math.ceil((end-start)/2.0))
    listLenght = len(collection)
    #print nbOfSwaps
    start %= listLenght
    end %= listLenght

    for i in range(nbOfSwaps):
        buff = collection[start]
        collection[start] = collection[end]
        collection[end] = buff
        start= (start+1)%listLenght
        end= (end-1)%listLenght

class KnotHash:
    def __init__(self, stringToHash):
        input = [ord(c) for c in stringToHash]
        input += [int(x) for x in '17, 31, 73, 47, 23'.split(', ')]

        key = range(256)
        skipSize = 0
        currIndex = 0

        for i in range(64):
            for lenght in input:
                reverseRange(key, currIndex, currIndex + lenght -1)
                currIndex+=lenght+skipSize
                skipSize+=1

        denseHash = []

        for i in range(16):
            element = key[16*i]
            for j in range(1, 16):
                element ^= key[16*i+j]
            denseHash.append(element)

        self._hash = ''.join([hex(e)[2:].zfill(2) for e in denseHash])

    def __str__(self):
        return self._hash

    def getHash(self):
        return self._hash

    def getBinaryHash(self):
        return bin(int('0x' + self._hash, 16))[2:].zfill(128)


input = 'xlqgujun'

knots = []

for i in range(0, 128):
    knots.append(KnotHash(input + '-' + str(i)))

grid = [[int(c) for c in knot.getBinaryHash()] for knot in knots]

def fill(x, y):
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
        return

    if grid[x][y] == 1:
        grid[x][y] = 0
        fill(x+1, y)
        fill(x-1, y)
        fill(x, y-1)
        fill(x, y+1)

print sum(k.getBinaryHash().count('1') for k in knots)

nbOfAreas = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 1:
            nbOfAreas+=1
            fill(i, j)

print nbOfAreas

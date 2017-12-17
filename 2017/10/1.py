import math

input = [ord(c) for c in open('input').readline().strip()]
input += [int(x) for x in '17, 31, 73, 47, 23'.split(', ')]

key = range(256)
skipSize = 0
currIndex = 0

def reverseRange(start, end):

    nbOfSwaps = int(math.ceil((end-start)/2.0))
    listLenght = len(key)
    #print nbOfSwaps
    start %= listLenght
    end %= listLenght

    for i in range(nbOfSwaps):
        buff = key[start]
        key[start] = key[end]
        key[end] = buff
        start= (start+1)%listLenght
        end= (end-1)%listLenght


for i in range(64):
    for lenght in input:
        reverseRange(currIndex, currIndex + lenght -1)
        currIndex+=lenght+skipSize
        skipSize+=1

denseHash = []

for i in range(16):
    element = key[16*i]
    #print element
    for j in range(1, 16):
        #print key[16*i+j]
        element ^= key[16*i+j]
        #print element
    denseHash.append(element)

#denseHash = [64, 7, 255]

#print denseHash

hash = ''.join([hex(e)[2:].zfill(2) for e in denseHash])
print hash


#print key
#print key[0]*key[1]

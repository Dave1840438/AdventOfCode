import sys

input = int(sys.argv[1])

dimension = 1

while dimension**2 < input:
    dimension+=2

offset = input - (dimension - 2) ** 2 - 1
print (dimension-1)/2 + abs(offset % (dimension-1) - ((dimension-1)/2 -1))

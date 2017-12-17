import sys

class Point(object):
    def __init__(self, x = 0, y = 0):
        self.X = x
        self.Y = y

    def move(self, tuple):
        self.X += tuple[0]
        self.Y += tuple[1]

    def add(self, tuple):
        return Point(self.X + tuple[0], self.Y + tuple[1])

input = int(sys.argv[1])
dimension = 100

MOVE_POSSIBILITIES = [(0, 1), (0, 0), (0, -1), (-1, 0), (-1, 1), (-1, -1), (1, 0), (1, -1), (1, 1)]

position = Point(dimension/2, dimension/2)

position.move((0, 1))

print position.X, position.Y

elements = []

for i in range(dimension):
    elements.append(dimension * [0])

elements[position.Y][position.X] = 1


print elements


def setValue():
    total = 0
    for m in MOVE_POSSIBILITIES:
        pos = position.add(m)
        total += elements[pos.Y][pos.X]

    elements[position.Y][position.X] = total
    return total


depth = 3

lastvalue = 0

found = False

while not found:
    position.move((1, 0))
    setValue()
    for i in range(depth-2):
        position.move((0, -1))
        lastvalue = setValue()
        if lastvalue > input:
            found = True
            print lastvalue


    for i in range(depth-1):
        position.move((-1, 0))
        lastvalue = setValue()
        if lastvalue > input:
            found = True
            print lastvalue

    for i in range(depth-1):
        position.move((0, 1))
        lastvalue = setValue()
        if lastvalue > input:
            found = True
            print lastvalue


    for i in range(depth-1):
        position.move((1, 0))
        lastvalue = setValue()
        if lastvalue > input:
            found = True
            print lastvalue


    depth += 2



class axial:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def add(self, ax):
        self.X += ax.X
        self.Y += ax.Y

DIRECTIONS = {'n': axial(1, -1), 'ne':axial(1, 0), 'se':axial(0, 1), 's':axial(-1, 1), 'sw':axial(-1, 0), 'nw':axial(0, -1)}

class hex:
    def __init__(self, x, y, z):
        self.X = x
        self.Y = y
        self.Z = z
        if x+y+z != 0:
            print 'INVALID HEX - ' + str(self)

    def __str__(self):
        return str('Hex: ' + ', '.join([str(self.X), str(self.Y), str(self.Z)]))

def hexDistance(lhs, rhs):
    return max(abs(lhs.X - rhs.X), abs(lhs.Y - rhs.Y), abs(lhs.Z - rhs.Z))

def axialToHex(ax):
    return hex(ax.X, ax.Y, -ax.X-ax.Y)


moves = open('input').readline().strip().split(',')

startingPoint = hex(0, 0, 0)
position = axial(0, 0)
maxDistance = 0

for move in moves:
    position.add(DIRECTIONS[move])
    maxDistance = max(hexDistance(startingPoint, axialToHex(position)), maxDistance)

print maxDistance
print hexDistance(startingPoint, axialToHex(position))

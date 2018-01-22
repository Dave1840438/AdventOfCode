class Point:
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    
    def add(self, other):
        self.X += other.X
        self.Y += other.Y
    
    def toTuple(self):
        return (self.X, self.Y)
    
    def __str__(self):
        return 'Point: ' + str(self.X) + ' ' + str(self.Y)
    
directions = [Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]

input = [line.strip() for line in open('input').readlines()]

grid = {}
for i in xrange(len(input)):
    for j in xrange(len(input)):
        grid[(j, i)] = input[i][j]

print grid
        
position = Point(len(input)/2, len(input[len(input)/2])/2)
direction = 3
#print position
infectionCount = 0
for i in xrange(10000):
    currPos = position.toTuple()
    
    if currPos not in grid:
        grid[currPos] = '.'
    
    direction = (direction + (1 if grid[currPos] == '#' else -1)) % len(directions)
    grid[currPos] = '#' if grid[currPos] == '.' else '.'
    if grid[currPos] == '#':
        infectionCount+=1
    position.add(directions[direction])

print infectionCount



    

from string import uppercase

class Point:
	def __init__(self, x, y):
		self.X = x
		self.Y = y
	
	def add(self, other):
		self.X += other.X
		self.Y += other.Y
		
startingPosition = Point(5, 0)

input = open('input').readlines()

grid = [[c for c in line.rstrip('\n\r')] for line in input]

#print grid

directions = {'down' : Point(0, 1), 'up' : Point(0, -1), 'right' : Point(1, 0), 'left' : Point(-1, 0)}

currChar = 'a'
currPos = Point(grid[0].index('|'), 0)
currDirection = 'down'
lettersVisited = []
steps = 0

while currChar != ' ':
	currChar = grid[currPos.Y][currPos.X]
	#print currChar
	if currChar == '+':
		for key, value in directions.iteritems():
			buffDir = directions[currDirection]
			if not(buffDir.X == -value.X and buffDir.Y == -value.Y):
				characterToFind = '-' if key == 'left' or key == 'right' else '|'
				tempPos = Point(currPos.X, currPos.Y)
				tempPos.add(value)
				if tempPos.Y >= 0 and tempPos.Y < len(grid) and tempPos.X >= 0 and tempPos.X < len(grid[tempPos.Y]):
					gridChar = grid[tempPos.Y][tempPos.X]
					if  gridChar == characterToFind or gridChar in uppercase:
						currDirection = key
						break
						#print currDirection
	elif currChar not in '-| ':
		lettersVisited.append(currChar)
	
	currPos.add(directions[currDirection])
	steps+=1

print ''.join(lettersVisited)
print steps-1

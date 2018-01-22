class Point:
	def __init__(self, x, y, z):
		self.X = x
		self.Y = y
		self.Z = z
	
	def sum(self):
		return abs(self.X) + abs(self.Y) + abs(self.Z)
	
	def __str__(self):
		return '(' + str(self.X) + ', ' + str(self.Y) + ', ' + str(self.Z) + ')'
	
	def __eq__(self, other):
		return self.X == other.X and self.Y == other.Y and self.Z == other.Z
		
	def add(self, point):
		self.X += point.X
		self.Y += point.Y
		self.Z += point.Z

class Particle:
	def __init__(self, p, v, a):
		self.P = p
		self.V = v
		self.A = a
	
	def __str__(self):
		return 'p = ' + str(self.P) + ', v = ' + str(self.V) + ', a = ' + str(self.A)
		
	def getAbsAcceleration(self):
		return self.A.sum()
	
	def __eq__(self, other):
		return self.P == other.P
	
	def samePosition(self, other):
		return self.P == other.P
	
	def move(self):
		self.V.add(self.A)
		self.P.add(self.V)

input = open('input').readlines()
particles = []

for l in input:
	data = l.strip().split(', ')
	params = []
	for d in data:
		digits = [int(digit.strip()) for digit in d[d.index('<')+1:d.index('>')].split(',')]
		params.append(Point(digits[0], digits[1], digits[2]))
	
	particles.append(Particle(params[0], params[1], params[2]))
	
unsortedParticles = [p for p in particles]
particles.sort(key=Particle.getAbsAcceleration)

print unsortedParticles.index(particles[0])


print len(particles)

particles = [p for p in particles if particles.count(p) == 1]

for i in xrange(50):
	for p in particles:
		p.move()
	particles = [p for p in particles if particles.count(p) == 1]
	
print len(particles)

#print particles[0]
	
	

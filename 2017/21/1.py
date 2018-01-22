from operator import add

class Grid:
    def __init__(self, lineGrid):
        self.gridFromLine(lineGrid)

    def gridFromLine(self, lineGrid):
        self._grid = [[c for c in line] for line in lineGrid.split('/')]

    def replace(self, patterns):
        #print self._grid
        for pattern in patterns:
            match = False
            for p in pattern.getPatterns():
                match |= self._grid == p


            if match:
                #print match
                self.gridFromLine(pattern._replace)
                break

    def __str__(self):
        return '\n'.join([''.join(line) for line in self._grid])

    def __iter__(self):
        return iter(self._grid)

    def getOnCount(self):
        counter = 0
        for line in self._grid:
            counter+=line.count('#')
        return counter

    def explode(self):
        chunkSize = 2 if len(self._grid) % 2 == 0 else 3
        nbOfChunks = len(self._grid) / chunkSize
        chunks = []
        #print chunkSize, len(self._grid), nbOfChunks
        for i in range(nbOfChunks):
            chunks.append([])
            for j in range(nbOfChunks):
                lines = []
                for k in range(chunkSize):
                    lines.append(''.join(self._grid[i*chunkSize+k][j*chunkSize:j*chunkSize+chunkSize]))
                chunks[i].append(Grid('/'.join(lines)))

        return chunks

    @staticmethod
    def join(chunks):
        chunkSize = len(chunks[0][0]._grid)
        grid = ['']*(len(chunks)*chunkSize)
        #print len(grid)
        for i in xrange(len(chunks)):
            for j in xrange(len(chunks)):
                for k in xrange(chunkSize):
                    grid[i*chunkSize+k]+=''.join(chunks[i][j]._grid[k])

        return Grid('/'.join([''.join(line) for line in grid]))


class Pattern:
    def __init__(self, pattern):
        data = pattern.strip().split(' => ')
        self._pattern = [[c for c in line] for line in data[0].split('/')]
        self._replace = data[1]

    def getPatterns(self):
        for i in xrange(2):
            for j in xrange(4):
				yield self._pattern
				self._pattern = [list(line[::-1]) for line in zip(*self._pattern)]
            self._pattern = [list(line[::-1]) for line in self._pattern]

    def __str__(self):
        for line in self._pattern:
            print ''.join(line)


grid = Grid('.#./..#/###')
input = open('input').readlines()
patterns = [Pattern(p) for p in input]

#for p in patterns[0].getPatterns():
#    print p
#    for c in p:
#        print ''.join(c)
#    print ''


#grid.replace(patterns)
for i in xrange(7):
    exploded = grid.explode()
    for layer in exploded:
        for tempGrid in layer:
            #print tempGrid
            tempGrid.replace(patterns)
            #print tempGrid
    #print exploded
    grid = Grid.join(exploded)
    print i

print grid
print grid.getOnCount()


#print Grid.join(exploded)

#    print '-------'
#print ''
#print grid

class Grid:
    def __init__(self, grid):
        self._grid = grid

    def replace(self, patterns):
        for pattern in patterns:
            p = pattern.strip().split('/')
            p = [[c for c in line] for line in p]
            print p

    def __str__(self):
        for line in grid:
            print ''.join(line)

class Pattern:
    def __init__(self, pattern):
        data = pattern.strip().split(' => ')
        self._pattern = [[c for c in line] for line in data[0].split('/')]
        self._replace = [[c for c in line] for line in data[1].split('/')]

    def getPatterns(self):
        for i in xrange(2):
            yield self._pattern
            for j in xrange(3):
                self.

    def __str__(self):
        for line in self._pattern:
            print ''.join(line)


grid = Grid([['.', '#', '.'], ['.','.','#'], ['#','#','#']])
input = open('input').readlines()

for p in input:
    p = Pattern(p)
    for pat in p.getPatterns():
        print pat

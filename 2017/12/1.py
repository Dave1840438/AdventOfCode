input = open('input').readlines()
groups = [[int(x[0])] + [int(y) for y in x[1].strip().split(',')] for x in [data.split(' <-> ') for data in input]]
groups = [set(x) for x in groups]

#print groups

intersectionFound = True

while intersectionFound:
    intersectionFound = False
    for i in range(len(groups)):
            for j in range(len(groups)):
                if j != i and len(groups[i].intersection(groups[j]))>0:
                    intersectionFound = True
                    groups[i].update(groups[j])
                    groups[j] = set()
    #print '-------------------------'
    #print groups

groups = [x for x in groups if len(x) > 0]

for g in groups:
    if 0 in g:
        print len(g)

print len(groups)

components = [(int(x), int(y)) for x, y in [line.strip().split('/') for line in open('input').readlines()]]
    
#print starter
#print '--'
#print components

bridges = []



for i in range(len(components)):
    if 0 in components[i]:
        for j in xrange(len(components)):
            if j != i:
                connection = max(components[i])
                if connection in components[j]:
                    bridges.append([i, j])


constructing = True
checkedBridges = 0
while constructing:
    constructing = False
    currStart = checkedBridges
    checkedBridges = len(bridges)
    for i in xrange(currStart, checkedBridges):
        for j in xrange(len(components)):
            if not j in bridges[i]:
                binding = components[bridges[i][-1]][0] if components[bridges[i][-1]][0] not in components[bridges[i][-2]] else components[bridges[i][-1]][1]
                if components[j][0] == binding or components[j][1] == binding:
                    bridges.append(list(bridges[i]) + [j])
                    constructing = True

#print components
#print bridges

bridges = [[components[x] for x in b] for b in bridges]

maxStrength = 0
maxLenght = 0
for b in bridges:
    if len(b) >= maxLenght:
        if maxLenght != len(b):
            maxStrength = 0
            maxLenght = len(b)
        maxStrength = max(maxStrength, sum(sum(x) for x in b))

print maxStrength

#answer is not 102

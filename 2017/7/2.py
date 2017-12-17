lines = open('input').readlines()

parents = {}
weights = {}
children = {}


for l in lines:
    data = l.split('->')
    parentName = data[0][:data[0].find(' ')]
    weights[parentName] = int(data[0][data[0].find('(')+1:data[0].find(')')])

    if (len(data) > 1):
        parents[parentName] = data[1].strip()

        for childName in data[1].split(', '):
            children[childName.strip()] = parentName


def getWeight(programName):
    w = weights[programName]
    if programName in parents:
        for child in parents[programName].split(', '):
            w += getWeight(child)

    return w

def isBalanced(programName):
    weights = [getWeight(x) for x in parents[programName].split(', ')]
    return all(w == weights[0] for w in weights)

def findRootProgram():
    for parent in children.values():
        if parent not in children.keys():
            return parent

def findProblemRoot(programName):
    for child in parents[programName].split(', '):
        #print child + ' ' + str(isBalanced(child))
        if not isBalanced(child):
            return findProblemRoot(child)



    return programName


probRoot = findProblemRoot(findRootProgram())

childWeights = [getWeight(x) for x in parents[probRoot].split(', ')]
childWeights.sort()


oddOne = childWeights[0] if childWeights[0] != childWeights[1] else childWeights[-1]
normalOne = next(w for w in childWeights if w != oddOne)

#print childWeights
#print (oddOne - normalOne)
#print probRoot
#print weights

print weights[next(x for x in parents[probRoot].split(', ') if getWeight(x) == oddOne)]  - (oddOne - normalOne)

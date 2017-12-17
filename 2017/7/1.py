lines = open('input').readlines()

parents = {}

for l in lines:
    data = l.split('->')
    #print data

    if (len(data) > 1):
        parentName = data[0][:data[0].find(' ')]
        for childName in data[1].split(', '):
            parents[childName.strip()] = parentName

#print parents

for parent in parents.values():
    if parent not in parents.keys():
        print parent
        break

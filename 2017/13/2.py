input = open('input').readlines()
lenghts = {}

for l in input:
    data = l.strip().split(': ')
    lenghts[int(data[0])] = int(data[1])

layers = [None] * (max(lenghts.keys()) + 1)

def isCaught(offset):
    for i in range(len(layers)):
        layers[i] = (i+offset) % (2*(lenghts[i]-1)) == 0 if i in lenghts else False
        if layers[i]:
            return True

    return False


offset = 0

while isCaught(offset):
    offset+=1


print offset

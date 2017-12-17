instructions = [int(x) for x in open('input').readlines()]

counter = 0
rip = 0

print len(instructions)

while rip >= 0 and rip < len(instructions):
    buff = rip
    rip += instructions[rip]
    instructions[buff] += -1 if instructions[buff] >= 3 else 1
    counter+=1

print counter

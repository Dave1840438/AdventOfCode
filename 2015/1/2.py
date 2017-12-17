input = open('input').readline()

floor = 0
counter = 0
for c in input:
    floor += 1 if c == '(' else -1
    counter+=1
    if floor == -1:
        break

print counter

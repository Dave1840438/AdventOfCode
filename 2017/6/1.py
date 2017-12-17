input = [int(x) for x in open('input').readline().split()]


def distribute():
    currIndex = input.index(max(input))
    buff = input[currIndex]
    input[currIndex] = 0

    for i in range(buff):
        currIndex+=1
        currIndex%=len(input)
        input[currIndex] += 1

knownConfigs = [list(input)]

counter = 0
while True:
    distribute()
    counter+=1

    if input in knownConfigs:
        break

    knownConfigs.append(list(input))

print input
print counter
print counter - knownConfigs.index(input)

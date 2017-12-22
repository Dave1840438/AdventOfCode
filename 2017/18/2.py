from string import digits
from collections import deque

registers = [{'p': 0}, {'p': 1}]

def isNumeric(string):
    return all(c in digits+'-' for c in string)

def initRegister(element, programId):
    if not(isNumeric(element)) and not(element in registers[programId]):
        registers[programId][element] = 0

def getValue(element, programId):
    if isNumeric(element):
        return int(element)

    return registers[programId][element]


input = open('input').readlines()

rips = [0, 0]
dataQueues = [deque(), deque()]

counter = 0

def run(programId):
    global counter

    executedOneInstruction = False

    otherProgramID = (programId + 1)%2

    while True:
        data = input[rips[programId]].strip().split()

        for value in data[1:]:
            initRegister(value, programId)

        if data[0] == 'snd':
            dataQueues[otherProgramID].append(getValue(data[1], programId))

            if programId == 1:
                counter += 1
        elif data[0] == 'set':
            registers[programId][data[1]] = getValue(data[2], programId)
        elif data[0] == 'add':
            registers[programId][data[1]] += getValue(data[2], programId)
        elif data[0] == 'mul':
            registers[programId][data[1]] *= getValue(data[2], programId)
        elif data[0] == 'mod':
            registers[programId][data[1]] %= getValue(data[2], programId)
        elif data[0] == 'rcv':
            if (len(dataQueues[programId]) > 0):
                registers[programId][data[1]] = dataQueues[programId].popleft()
            else:
                return executedOneInstruction
        elif data[0] == 'jgz':
            if getValue(data[1], programId) > 0:
                rips[programId] += getValue(data[2], programId)
                continue

        rips[programId]+=1

        executedOneInstruction = True

notInDeadLock = True
while notInDeadLock:
    notInDeadLock = run(0)
    notInDeadLock |= run(1)



print registers
print counter

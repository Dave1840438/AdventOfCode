from string import digits

registers = {}

def isNumeric(string):
    return all(c in digits+'-' for c in string)

def initRegister(element):
    if not element in registers:
        registers[element] = 0

def getValue(element):
    if isNumeric(element):
        return int(element)

    return registers[element]


input = open('input').readlines()

lastPlayedFreqency = 0
rip = 0

while True:
    data = input[rip].strip().split()

    for value in data[1:]:
        initRegister(value)

    if data[0] == 'snd':
        lastPlayedFreqency = getValue(data[1])
    elif data[0] == 'set':
        registers[data[1]] = getValue(data[1])
    elif data[0] == 'add':
        registers[data[1]] += getValue(data[1])
    elif data[0] == 'mul':
        registers[data[1]] *= getValue(data[1])
    elif data[0] == 'mod':
        registers[data[1]] %= getValue(data[1])
    elif data[0] == 'rcv':
        if getValue(data[1]) != 0:
            break
    elif data[0] == 'jgz':
        if getValue(data[1]) > 0:
            rip += getValue(data[2])
            continue

    rip+=1

print lastPlayedFreqency

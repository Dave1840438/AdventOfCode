from string import digits

registers = {}

def isNumeric(string):
    return all(c in digits+'-' for c in string)

def initRegister(element):
    if not(isNumeric(element)) and not(element in registers):
        registers[element] = 0

def getValue(element):
    if isNumeric(element):
        return int(element)

    return registers[element]


input = open('input').readlines()

counter = 0
rip = 0

while True:
    if rip < 0 or rip >= len(input):
        break
        
    data = input[rip].strip().split()

    for value in data[1:]:
        initRegister(value)

    if data[0] == 'set':
        registers[data[1]] = getValue(data[2])
    elif data[0] == 'sub':
        registers[data[1]] -= getValue(data[2])
    elif data[0] == 'mul':
        registers[data[1]] *= getValue(data[2])
        counter+=1
    elif data[0] == 'jnz':
        if getValue(data[1]) != 0:
            rip += getValue(data[2])
            continue

    rip+=1

print registers
print counter

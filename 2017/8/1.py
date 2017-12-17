from string import digits

registers = {}

def isNumeric(string):
    return all(c in digits+'-' for c in string)

def initRegister(register):
    if register not in registers:
        print 'init: ' + register
        registers[register] = 0

def compute(instruction):
    parts = instruction.strip().split(' ')
    register = "registers['" + parts[0] + "']"

    initRegister(parts[0])

    if not isNumeric(parts[4]):
        initRegister(parts[4])
        parts[4] = "registers['" + parts[4] + "']"

    if not isNumeric(parts[6]):
        initRegister(parts[6])
        parts[6] = "registers['" + parts[6] + "']"

    print ' '.join(parts[4:])
    if eval(' '.join(parts[4:])):
        operator = '+' if parts[1] == 'inc' else '-'
        registers[parts[0]] = eval(register + operator + parts[2])

instructions = open('input').readlines()

maxValue = 0

for i in instructions:
    compute(i)
    maxValue = max(max(registers.values()), maxValue)

print max(registers.values())
print maxValue

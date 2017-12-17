previousA = 516
previousB = 190

dividingFactor = 2147483647
mask = 2**16

counter = 0

for i in range(5000000):
    previousA = (previousA * 16807) % dividingFactor
    while previousA % 4 != 0:
        previousA = (previousA * 16807) % dividingFactor

    previousB = (previousB * 48271) % dividingFactor
    while previousB % 8 != 0:
        previousB = (previousB * 48271) % dividingFactor

    #print previousA, previousB

    if (previousA % mask) ^ (previousB % mask) == 0:
        counter+=1

print counter

previousA = 65
previousB = 8921

dividingFactor = 2147483647
mask = 2**16-1

counter = 0

for i in range(40000000):
    previousA = (previousA * 16807) % dividingFactor
    previousB = (previousB * 48271) % dividingFactor
    #print previousA, previousB
    if (previousA & mask) ^ (previousB & mask) == 0:
        counter+=1

print counter

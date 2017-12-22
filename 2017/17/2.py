step = 354

currIndex = 0
highest = 0

i = 1
while i < 50000000:
    currIndex = ((currIndex + step) % i) + 1

    if (currIndex == 1):
        highest = i

    i+=1

print highest

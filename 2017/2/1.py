input = open('input').readlines()

checksum = 0

for l in input:
    numbers = [int(x) for x in l.split()]
    checksum += max(numbers) - min(numbers)

print checksum

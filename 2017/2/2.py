from itertools import product

input = open('input').readlines()

checksum = 0

for l in input:
    numbers = [int(x) for x in l.split()]
    combinations = list(product(numbers, repeat = 2))
    #print combinations
    solution = filter(lambda x: x[0] != x[1] and x[0] % x[1] == 0, combinations)
    checksum += solution[0][0]/solution[0][1]

print checksum

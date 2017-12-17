input = open('input').readline().strip()
halfLenght = len(input)/2

print sum([int(x) * 2 for x, y in zip(input[:halfLenght], input[-halfLenght:]) if x == y])

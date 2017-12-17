input = open('input').readline().strip()
input+=input[0]

total = 0

for i in range(0, len(input)-1):
    if input[i] == input[i+1]:
        total+=int(input[i])

print total

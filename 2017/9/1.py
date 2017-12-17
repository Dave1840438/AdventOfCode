from re import sub

input = list(open('input').readline())

for i in range(len(input)):
    if input[i] == '!':
        input[i] = 'c'
        input[i+1] = 'c'

print ''.join(input)

garbage = 0
erasing = False
for i in range(len(input)):
    if erasing:
        if input[i] == '>':
            erasing = False
        elif input[i] != 'c':
            garbage+=1
        input[i] = '0'
    else:
        if input[i] == '<':
            input[i] = '0'
            erasing = True


print ''.join(input)

totalScore = 0
depth = 0

for c in input:
    if c == '{':
        depth+=1
    if c == '}':
        totalScore+=depth
        depth-=1



input = sub('0*', '', ''.join(input))


print input
print totalScore
print garbage

from collections import deque


programs = [chr(x) for x in range(97, 113)]

instructions = open('input').readline().strip()

counter = 0
while counter < 70:
	for instruction in instructions.split(','):
		if instruction[0] == 's':
			rot = int(instruction[1:])
			programs = programs[-rot:] + programs[:-rot]
		elif instruction[0] == 'x':
			data = instruction[1:].split('/')
			a = int(data[0])
			b = int(data[1])
			buff = programs[a]
			programs[a] = programs[b]
			programs[b] = buff
		elif instruction[0] == 'p':
			data = instruction[1:].split('/')
			a = programs.index(data[0])
			b = programs.index(data[1])
			buff = programs[a]
			programs[a] = programs[b]
			programs[b] = buff

	counter += 1

	if programs == sorted(programs):
		print '!!!'

print ''.join(programs)

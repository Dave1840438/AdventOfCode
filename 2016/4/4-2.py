from collections import Counter

lines = open('input').readlines()
output = open('output', 'w')

result = 0

for l in lines:
	checksum = l[l.index('[') + 1 : l.index(']')]

	encName = l[0:l.index('[')].split('-')
	sectorID = int(encName[-1])

	decName = ""

	for c in (' '.join(encName[0:-1])):
		if c.isalpha():
			decName += chr((ord(c) - ord('a') + sectorID) % 26 + ord('a'))
		else:
			decName += c

	output.write(decName + " ; " + str(sectorID) + "\n")
	#print decName


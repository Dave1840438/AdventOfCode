from collections import Counter

lines = open('input').readlines()

result = 0

for l in lines:
	checksum = l[l.index('[') + 1 : l.index(']')]

	encName = l[0:l.index('[')].split('-')
	sectorID = encName[-1]
	letters = Counter(''.join(encName[0:-1]))

	computedHash = ''.join([x for x, y in sorted(letters.most_common(), key=lambda e : (-e[1], e[0]))[:5]])

	print computedHash
	if (checksum == computedHash):
		result = result + int(sectorID)

print result
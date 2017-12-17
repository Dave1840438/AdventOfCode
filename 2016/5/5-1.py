import hashlib


puzzleInput = 'ugkcyxxp'

counter = 0
index = 0
result = ''

while counter < 8:
	digest = hashlib.md5(puzzleInput + str(index)).hexdigest()
	if digest.startswith('00000'):
		result += digest[5]
		counter += 1
	index+=1


print result



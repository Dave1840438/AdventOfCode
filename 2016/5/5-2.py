import hashlib


puzzleInput = 'ugkcyxxp'

counter = 0
index = 0
result = [''] * 8

while counter < 8:
	digest = hashlib.md5(puzzleInput + str(index)).hexdigest()
	if digest.startswith('00000'):
		position = int(digest[5]) if digest[5].isdigit() else 8
		#print digest
		#print position

		if (position < 8):

			if result[position] == '':
				result[position] = digest[6]
				counter += 1

			

			
	index+=1


print ''.join(result)



from collections import Counter

lines = open('input').readlines()
#Get the last element à la place du premier pour solve la deuxième partie
word = ''.join([Counter([l[i] for l in lines]).most_common()[0][0] for i in range(len(lines[0]))]).strip()

print word 

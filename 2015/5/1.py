naughtySubstrings = ['ab', 'cd', 'pq', 'xy']
vowels = 'a e i o u'.split()

def findAdjacentLetters(string):
    lastLetter = string[0]
    for i in range(1, len(string)-1):
        if lastLetter == string[i]:
            return True
        lastLetter = string[i]

    return False

def isNice(string):
    if any(string.find(x) != -1 for x in naughtySubstrings):
        return False

    if sum(1 for x in string if x in vowels) < 3:
        return False

    return findAdjacentLetters(string)

print sum(1 for s in open('input').readlines() if isNice(s))

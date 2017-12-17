from re import sub, findall

regex = r'\[[a-z]*\]'

def supportsTLS(string):

    if any(isABBA(x) for x in findall(regex, string)):
        return False

    outsideElements = sub(regex, ' ', string).split(' ')

    return any(isABBA(x) for x in outsideElements)

def isABBA(string):
    for i in range(len(string) -3):
        if (string[i] == string[i+3] and string[i+1] == string[i+2] and string[i] != string[i+1]):
            return True

    return False




input = open('input').readlines()

print sum(1 for l in input if supportsTLS(l))

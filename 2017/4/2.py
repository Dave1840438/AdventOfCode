lines = open('input').readlines()

def isValid(string):
    words = [''.join(sorted(w)) for w in string.split()]


    for word in words:
        if words.count(word) != 1:
            return False

    return True

print sum(1 for l in lines if isValid(l))

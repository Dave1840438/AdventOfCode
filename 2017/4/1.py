import collections
print sum(1 for l in open('input').readlines() if not(any(c != 1 for c in collections.Counter(l.split()).values()))

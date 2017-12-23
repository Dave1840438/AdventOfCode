def isPrime(n):
    for i in range(2, n/2):
        if n % i  == 0:
            return False
    
    return True
    
    
print sum(1 for i in xrange(106500, 123501, 17) if not isPrime(i))

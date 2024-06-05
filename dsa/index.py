def isPrime(a):
    if a == 1:
        return False
    i = 2
    while(i*i <= a):
        if a %i == 0:
            return False
        i += 1
        return True

print(isPrime(5))
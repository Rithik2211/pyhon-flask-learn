# stieve of erasthoensis

def isPrime(n):
    if n == 1:
        return False
    if n ==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while (i*i <= n):
        if (n%i == 0 or n%(i+2)==0):
            return False
        i+=6
    return True

def soe(num):
    a = []
    for i in range(2, num+1):
        if isPrime(i):
            a.append(i)

    return a

print(soe(23))

def median(arr):
    n = len(arr)
    arr.sort()
    if n % 2 == 0:
        return (arr[n//2] + arr[n//2 - 1]) / 2
    else:
        return arr[n//2]
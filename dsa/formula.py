'''
 1) print sum of all the numbers in the given series :  n * (n+1) // 2

 2) print celcius to fahrenheit :   (c * 9/5) + 32     # 32 degree offset

 3) print fahrenheit to celcius :  (f - 32) * 5/9       # 32 degree offset

 4) count length of the numbers : math.floor(math.log10(N)+1)     # import math | T-complexity -> O(1)

 5) factorial of the numbers in recursion :  n * fact(n-1) 

 6) Digits of the factorial : 
    def digitsInFactorial(self,N):
        if N==0 or N==1:
            return 1
        digit = 0
        for i in range(2, N+1):
            digit += math.log10(i)
        return math.floor(digit +1)

 7) Find the Trailing of the zeros :
    def findTrailingZeros(n):
        count = 0
        # Keep dividing n by powers of 5 and update Count
        i = 5
        while (n / i>= 1):
            count += int(n / i)
            i *= 5

        return int(count)
    
8) GCD and HCF of two numbers : 
    def gcd(a,b):
        if b==0:
            return a
        return gcd(b,a%b)

 
9) An efficient solution is based on the below formula for LCM of two numbers ‘a’ and ‘b’. 
   a x b = LCM(a, b) * GCD (a, b)
   LCM(a, b) = (a x b) / GCD(a, b)
   solution : 

    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b, a%b)
    def lcm(a,b):
        return a * b // gcd(a,b)

10) Check for the prime : 
   worst case O(n)
    def isPrime(n):
        if n ==1 :
            return False
        for i in range(2, n):
            if n%i == 0:
                return False
        return True

    - Divisors are always appear in the pair
    - if (a,b) if a <= b ->  (a*a <= b) or (a <= sqrt(b))

    best case O(sqrt(n)):
    def checkPrime(n):
        if n == 1:
            return False
        i = 2
        while (i*i <= n):
            if n%i == 0:
                return False
            i += 1
        return True
    
    super efficient way :

    def primeSuperEff(n):
        if n==1:
            return False
        if n==2 or n==3:
            return True
        if n%2 == 0 or n%3 == 0:
            return False
        i = 5
        while(i*i <= n):
            if (n%i == 0 or n % (i+2) == 0):
                return False
            i +=6
        return True 

11) Prime Factor of number :

def isPrime(n):
    if n==1:
        return False
    if n==2 or n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    i=5
    while (i*i <= n):
        if n%i==0 or n%(i+2)==0:
            return False
        i+=6
    return True

a = []
def primeFactor(n):
    for i in range(2,n+1):
        if isPrime(i):
            x = i
            while n%x == 0:
                a.append(i)
                x *= i
    
'''
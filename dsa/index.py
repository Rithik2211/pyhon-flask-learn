def printDivisors(n):
    i=1
    while((i*i) < n):  # divisors from 1 to root n excuded
        if(n%i == 0) :
            print(i)
        i+=1
    while (i >= i): # divisors from root n includes from 1
        if(n%i == 0):
            print(n//i)
        i-=1


printDivisors(25)
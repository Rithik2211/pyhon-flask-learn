import math
a = 8234


# print(a *(a+1) // 2)
# print(math.floor(math.log10(a)+1))

def fact(n):
    if n==0 or n==1:
        return 1
    digit = 0
    for i in range(2, n+1):
        digit += math.log10(i)
    return math.floor(digit+1)

print(fact(5))
        
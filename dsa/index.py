a = [12,1,4,6,3,1,8,10]

def bubbleSort(a):
    for i in range(len(a)-1):
        swapped = False
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped :
            break
    return a

def selectionSort(a):
    for i in range(len(a)-1):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a

print(selectionSort(a))
            
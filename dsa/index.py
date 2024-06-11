a = [2,4,6,2,1,7,3,5]

def bubbleSort(a) :
    for i in range(len(a)-1):
        sorted = False
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                sorted = True
                a[j], a[j+1] = a[j+1], a[j]
        if not sorted:
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

def insertionSort(a):
    for i in range(1, len(a)):
        key = i
        val = a[i]
        for j in range(i-1, -1, -1):
            if a[j] > val:
                a[j+1] = a[j]
                key = j
            else:
                break
        a[key] = val
    return a


print(bubbleSort(a))
print(selectionSort(a))
print(insertionSort(a))
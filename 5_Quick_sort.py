import matplotlib.pyplot as plt
import random
import time as t

def quickSort(a,low,high):
    if low < high:
        pivot = partition(a,low,high)
        quickSort(a,low,pivot-1)
        quickSort(a,pivot+1,high)

def partition(a,low,high):
    pivot = a[low]
    i = low + 1
    j = high
    
    while True:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[i] > pivot:
            j -= 1
        if i < j:
            a[i],a[j] = a[j],a[i]
        else:
            break
    
    a[low] , a[j] = a[j] , a[low]
    return j

if __name__ == "__main__":
    x = []
    y = []
    
    for n in range(100,10000,100):
        a = [random.randint(1,n) for _ in range(n)]
        x.append(n)
        print("Size of arr",n)
        
        start= t.time()
        quickSort(a,0,len(a)-1)
        end = t.time()
        gap = end - start
        
        y.append(gap)
        print("sorted array:",a[:20])
        
    plt.plot(x,y,label="Quick Sort")
    plt.xlabel("Input Size")
    plt.ylabel("Time")
    plt.grid(True)
    plt.legend()
    plt.show()
import matplotlib.pyplot as plt
import time as t
import random

def divide(a,low,high):
    if low < high:
        mid = (low + high) // 2
        divide(a,low,mid)
        divide(a , mid + 1 , high)
        merge(a,low,mid,high)

def merge(a,low,mid,high):
    temp = [0] * (high - low + 1)
    i = low
    j = mid + 1
    k = 0
    
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            temp[k] = a[i]
            i+=1
        else:
            temp[k] = a[j]
            j+=1
        k+=1
    
    while i <= mid :
        temp[k] = a[i]
        i+=1
        k+=1
    
    while j <= high:
        temp[k] = a[j]
        j+=1
        k+=1
        
    for i in range(low,high+1):
        a[i] = temp[i-low]
        
if __name__ == "__main__":
    x = []
    y = [] 
    
    for n in range(1000,10001,1000):
        a = [random.randint(1,n) for _ in range(n)]
        x.append(n)
        
        start = t.time()
        divide(a,0, len(a) - 1)
        end = t.time()
        gap = end - start
        
        y.append(gap)
        
    plt.plot(x,y,label = "Merge Sort")
    plt.xlabel("n Size")
    plt.ylabel("Time")
    plt.legend()
    plt.show()
#Bubble sort and Selection Sort
import matplotlib.pyplot as plt
import time
from random import randint

def BubbleSort(a,n):
    for i in range (0,n-1):
        for j in range(0,n-1-i):
            if(a[j+1]<a[j]):
                a[j],a[j+1] = a[j+1],a[j]

def Selectionsort(a,n):
  for i in range (n-1):
    min = i
    for j in range (i + 1 , n):
      if (a [j] < a[min]):
        min=j
    a[i] , a[min] = a[min],a[i]

if __name__ == "__main__":
    x=[]
    y1=[]
    y2=[]
    for n in range(10,1001,10):
        a = []
        x.append(n)
        for i in range(n):
            a.append(randint(1,n))

        start = time.time()
        BubbleSort(a,n)
        end = time.time()
        gaptime = end - start
        y1.append(gaptime)

        start=time.time()
        Selectionsort(a,n)
        end=time.time()
        gaptime=end-start
        y2.append(gaptime)

    plt.plot(x,y1,label="Bubble Sort")
    plt.plot(x,y2,label="Selection Sort")
    plt.xlabel("n size")
    plt.ylabel("Time")
    plt.legend()
    plt.show()


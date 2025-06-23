import matplotlib.pyplot as plt
import time

def linearSearch(arr,key):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == key:
            print(f"Key found at pos: {i}")
            return count
    print("key not found")
    return count

def binarySearch(arr,key):
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low+high)//2
        if arr[mid] == key:
            print(f"Key found at position: {mid}")
            return count
        elif arr[mid] > key:
            high = mid - 1
        else:
            low = mid + 1
    print("Key not found")
    return count

if __name__ == "__main__":
    n = int(input("Enter the size of the array: "))
    arr = list(range(n))
    print("Array: ",arr)
    
    key = int(input("Enter the key to search: "))
    
    start = time.time()
    Lcount = linearSearch(arr,key)
    end = time.time()
    gap1 = end - start
    
    start = time.time()
    Bcount = binarySearch(arr,key)
    end = time.time()
    gap2 = end - start
    
    print("Number of comparisitons : ",Lcount)
    print("Number of comparisitons : ",Bcount)
    
    plt.bar(["linear Search","Binary Search"], [Lcount,Bcount])
    plt.xlabel("Search Algo")
    plt.ylabel("time")
    plt.show()
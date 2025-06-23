import matplotlib.pyplot as plt
import time

def LinearSearch(a, n, key):
    Lcount = 0
    for i in range(n):
        Lcount += 1
        if a[i] == key:
            print(f"Key found at pos: {i}")
            return Lcount
    print("Key not found")
    return Lcount

def BinarySearch(a, n, key):
    Bcount = 0
    low = 0
    high = n - 1
    while low <= high:
        Bcount += 1
        mid = (low + high) // 2
        if a[mid] == key:
            print(f"Key found at pos: {mid}")
            return Bcount
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print("Key not found")
    return Bcount

if __name__ == "__main__":
    n = int(input("Enter n: "))
    a = list(range(n))  # simplified
    print(a)
    key = int(input("Enter Key: "))

    # Linear Search
    start = time.perf_counter()
    Lcount = LinearSearch(a, n, key)
    end = time.perf_counter()
    Lgap = end - start

    # Binary Search
    start = time.perf_counter()
    Bcount = BinarySearch(a, n, key)
    end = time.perf_counter()
    Bgap = end - start

    print(f"Number of comparisons in Linear Search: {Lcount}")
    print(f"Number of comparisons in Binary Search: {Bcount}")

    # Plot
    plt.bar(['Linear Search', 'Binary Search'], [Lgap, Bgap], color=['red', 'green'])
    plt.xlabel("Search Algorithm")
    plt.ylabel("Time (seconds)")
    plt.title("Linear vs Binary Search Timing")
    plt.show()

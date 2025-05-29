#Quick Sort 
import matplotlib.pyplot as plt
import random
import time as t

def quick_sort(a, low, high):
    if low < high:
        j = partition(a, low, high)
        quick_sort(a, low, j - 1)
        quick_sort(a, j + 1, high)

def partition(a, low, high):
    pivot = a[low]
    i = low + 1
    j = high

    while True:
        while i <= j and a[i] <= pivot:
            i += 1
        while i <= j and a[j] > pivot:
            j -= 1
        if i < j:
            a[i], a[j] = a[j], a[i]
        else:
            break

    a[low], a[j] = a[j], a[low]
    return j

if __name__ == "__main__":
    x = []
    y = []

    for n in range(10000, 100001, 10000):
        a = [random.randint(1, n) for _ in range(n)]
        x.append(n)

        print(f"\nArray size: {n}")
        print("Random array (first 20 elements):", a[:20])

        start = t.time()
        quick_sort(a, 0, len(a) - 1)
        end = t.time()

        y.append(end - start)
        print("Sorted array (first 20 elements):", a[:20])

    plt.plot(x, y, color='cyan', marker='o', label='Quick Sort Time')
    plt.title("Quick Sort Time Complexity")
    plt.xlabel("Input size (n)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.show()

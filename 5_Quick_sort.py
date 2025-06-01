import matplotlib.pyplot as plt
import random
import time

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

if __name__ == "__main__":
    x = []
    y = []

    for n in range(10000, 100001, 10000):
        arr = [random.randint(1, n) for _ in range(n)]
        x.append(n)

        print(f"\nArray size: {n}")
        print("Random array (first 20 elements):", arr[:20])

        start_time = time.perf_counter()
        quick_sort(arr, 0, len(arr) - 1)
        end_time = time.perf_counter()

        y.append(end_time - start_time)
        print("Sorted array (first 20 elements):", arr[:20])

    # Plotting the results
    plt.plot(x, y, color='cyan', marker='o', label='Quick Sort Time')
    plt.title("Quick Sort Time Complexity")
    plt.xlabel("Input Size (n)")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

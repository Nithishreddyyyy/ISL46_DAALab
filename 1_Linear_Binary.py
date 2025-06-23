import matplotlib.pyplot as plt
import time

def linear_search(arr, key):
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == key:
            print("Key found at position:", i)
            return count
    print("Key not found")
    return count

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if arr[mid] == key:
            print("Key found at position:", mid)
            return count
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    print("Key not found")
    return count

# Main program
n = int(input("Enter the size of the array: "))
arr = list(range(n))
print("Array:", arr)

key = int(input("Enter the key to search: "))

# Linear Search
start = time.perf_counter()
l_count = linear_search(arr, key)
end = time.perf_counter()
l_time = end - start

# Binary Search
start = time.perf_counter()
b_count = binary_search(arr, key)
end = time.perf_counter()
b_time = end - start

print("\nNumber of comparisons in Linear Search:", l_count)
print("Number of comparisons in Binary Search:", b_count)

# Plotting the comparison
plt.bar(["Linear Search", "Binary Search"], [l_time, b_time], color=["red", "green"])
plt.xlabel("Search Algorithm")
plt.ylabel("Time (seconds)")
plt.title("Linear vs Binary Search Timing")
plt.show()

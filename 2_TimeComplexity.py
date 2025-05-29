#a. Find the sum of all elements in an array.

import matplotlib.pyplot as plt
import time as t
import random

def my_sum(a, n):
  total = 0
  for i in range(n):
    total += a[i]
  return total


if __name__ == "__main__":
  x = []
  y = []

  for n in range(10, 100, 10):
    a = [random.randint(1, n) for _ in range(n)]
    x.append(n)

    start = t.time()
    res = my_sum(a, n)
    end = t.time()

    gap = end - start
    y.append(gap)

    print(a)
    print("sum: ", res)

  plt.plot(x, y, label="Sum of elements in array")
  plt.xlabel("Input size n:")
  plt.ylabel("Time (sec)")
  plt.legend()
  plt.show()


#b. Find the binary equivalent of a given decimal number.

import time as t
import matplotlib.pyplot as plt

def decimal_to_binary(n):
    if n == 0:
        return "0"

    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
    return binary

'''
if __name__ == "__main__":
    x = []
    y = []

    for num in range(10, 1001, 50):
        start = t.time()
        binary_val = decimal_to_binary(num)
        end = t.time()
        gap = end - start

        x.append(num)
        y.append(gap)

        print("Binary equivalent of " + str(num) + " is: " + binary_val)

    plt.figure(figsize=(10,6))
    plt.plot(x, y,color='orange', label="Decimal to Binary Conversion Time")
    plt.xlabel("Decimal Input Value")
    plt.ylabel("Time (seconds)")
    plt.title("Time complexcity of decimal to binary conversion")
    plt.legend()
    plt.show()
'''

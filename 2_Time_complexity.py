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
    a = [random.randint(1,n) for _ in range(n)]
    x.append(n)

    start = t.time()
    res = my_sum(a, n)
    end = t.time()

    gap = end - start
    y.append(gap)
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
        binary += str(remainder)
        n = n // 2
    return binary

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


#c. Read a matrix and print only the even elements.

import matplotlib.pyplot as plt
import time
import numpy as np

def find_even_elements(matrix, rows, cols):
    even_elements = []
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] % 2 == 0:
                even_elements.append(matrix[i][j])
    return even_elements

if __name__ == "__main__":
    x = []
    y = []

    for n in range(100, 1001, 100):
        x.append(n * n)

        matrix = np.random.randint(1, 1000, size=(n, n))

        start_time = time.time()
        even_elements = find_even_elements(matrix, n, n)
        end_time = time.time()

        y.append(end_time - start_time)

    plt.plot(x, y, marker='o', linestyle='-', label='Time taken to find even elements')
    plt.xlabel("Input size (n × n)")
    plt.ylabel("Time (seconds)")
    plt.title("Time Complexity of Finding Even Elements in a Matrix")
    plt.legend()
    plt.grid(True)
    plt.show()

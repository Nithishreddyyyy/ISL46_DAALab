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



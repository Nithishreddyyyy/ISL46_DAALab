#Horspool's Algorithm
text = 'JIM_SAW_ME_IN_A_BARBER_SHOP'
pattern = 'BARBER'
n = len(text)
m = len(pattern)
shift = {}

def shift_table():
    for i in range(128):  # ASCII range
        shift[chr(i)] = m
    for i in range(m - 1):
        shift[pattern[i]] = m - 1 - i
    print('----Shift Table Ready----')
    for char in pattern:
        print(f"{char}: {shift[char]}")
    print()

def horspool():
    i = m - 1
    while i <= n - 1:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        i += shift.get(text[i], m)  # default shift if char not in pattern
    return -1

if __name__ == "__main__":
    shift_table()
    pos = horspool()
    print("Pattern found at index:", pos if pos != -1 else "Not found")

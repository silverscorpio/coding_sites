# Sorting porblem - Day 20! - Bubble Sort

n = int(input())
num_string = input()
a = num_string.split()
b = []
for i in a:
    b.append(int(i))
count = 0
numSwaps = 0
while count != n:
    for j in range(0, n - 1):
        if b[j] >= b[j+1]:
            c = b[j]
            b[j] = b[j+1]
            b[j+1] = c
            numSwaps += 1
        else:
            pass
    count += 1
print(f"""Array is sorted in {numSwaps} swaps.
First Element: {b[0]}
Last Element: {b[-1]}""")
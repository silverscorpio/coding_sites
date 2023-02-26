# hourglass - Problem 11

lines = 0
big = []
while lines < 6:
    line = input()
    big.append([int(i) for i in line.split()])
    lines += 1
count = 0
a = 0
b = 3
j = 0
k = 3
small = []
while b != 7:
    while k != 7:
        for i in range(a, b):
            small.append(big[i][j:k])
        j += 1
        k += 1
        count += 1
    a += 1
    b += 1
    j = 0
    k = 3
three = []
for p in range(0, len(small) - 2, 3):
    three.append([small[p],
                  small[p + 1],
                  small[p + 2]])
# print(f"No. of 3x3 matrices: {count}")
sumy = []
for q in three:
    alpha = sum(q[0]) + q[1][1] + sum(q[2])
    sumy.append(alpha)
print(max(sumy))
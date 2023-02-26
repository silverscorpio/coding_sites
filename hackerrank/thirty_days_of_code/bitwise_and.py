# BITSWISE AND - Day 29

t = int(input())
counter, data = 0, []
while counter < t:
    parts = input().split()
    data.append([int(parts[0]), int(parts[1])])
    counter += 1
count = 0
maxy = []
for numby in range(len(data)):
    n, k = data[numby][0], data[numby][1]
    listy = range(1, n + 1)
    max_AND = 0
    if k == n:
        for i in range(len(listy) - 3, len(listy)):
            for j in range(i + 1, len(listy)):
                compy = listy[i] & listy [j]
                if max_AND < compy < k:
                    max_AND = compy
                    if (compy == k - 1) or (compy == k - 2):
                            break
        maxy.append(max_AND)
    else:
        for i in range(k - 3, k):
            for j in range(i + 1, len(listy)):
                compy = listy[i] & listy [j]
                if max_AND < compy < k:
                    max_AND = compy
                    if (compy == k - 1) or (compy == k - 2):
                        break
        maxy.append(max_AND)
for k in maxy:
    print(k)
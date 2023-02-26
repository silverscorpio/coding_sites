### Exercise - 26 - Pythogorean Triplet

import math as m

def pyth_trip1(number):
    a = [(i ** 2) for i in range(1, number + 1)]
    b = [(i ** 2) for i in range(1, number + 1)]
    c = [(i ** 2) for i in range(1, number + 1)]
    triplets = []

    for i in a:
        for j in b:
            if j > i:
                for k in c:
                    if k > j:
                        if (i + j == k) and (int(m.sqrt(i)) + int(m.sqrt(j)) + int(m.sqrt(k)) == number):
                            triplets.append([int(m.sqrt(i)), int(m.sqrt(j)), int(m.sqrt(k))])

    return triplets

print(pyth_trip1(30000))


def pyth_trip2(number):
    a = range(1, number + 1)
    b = range(1, number + 1)
    c = range(1, number + 1)
    triplets = []

    for i in a:
        for j in b:
            if j > i:
                for k in c:
                    if k > j:
                        if ((i**2) + (j**2) == (k**2)) and (i + j + k == number):
                            triplets.append([i, j, k])

    return triplets

print(pyth_trip2(1000))
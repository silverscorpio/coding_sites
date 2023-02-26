# Problem 9

import math as m

def pyth_trip():
    a = []
    b = []
    c = []
    triplets = []
    prod = 1

    for alpha in range(1, 1001):
        a.append(alpha**2)
        b.append(alpha**2)
        c.append(alpha**2)

    for i in a:
        for j in b:
            if j > i:
                for k in c:
                    if k > j:
                        if (i + j == k) and (int(m.sqrt(i)) + int(m.sqrt(j)) + int(m.sqrt(k)) == 1000):
                            triplets.append([int(m.sqrt(i)), int(m.sqrt(j)), int(m.sqrt(k))])
                        else:
                            pass
                    else:
                        pass
            else:
                pass

    for z in triplets:
        for y in z:
            prod *= y

    print(f"Product of Pytho_Triplet: {prod}")
    print(f"Pytho_Triplet: {triplets}")

pyth_trip()
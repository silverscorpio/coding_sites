##### BINOMIAL DISTRIBUTION - 2

import math as m
vals = input().split()
pd = float(vals[0]) / 100
pnd = 1 - pd
n = int(vals[1])
part_a = 0
part_b = 0
for i in range(0,3):
    combi = (m.factorial(n)) / ((m.factorial(i)) * (m.factorial(n - i)))
    p = combi * (pd**i) * (pnd**(n - i))
    part_a += p

for i in range(2,11):
    combi = (m.factorial(n)) / ((m.factorial(i)) * (m.factorial(n - i)))
    p = combi * (pd**i) * (pnd**(n - i))
    part_b += p

print(round(part_a, 3))
print(round(part_b, 3))
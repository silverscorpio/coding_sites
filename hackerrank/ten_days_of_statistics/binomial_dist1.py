##### BINOMIAL DISTRIBUTION - 1

import math as m
vals = input().split()
ratio = float(vals[0])/float(vals[1])
pg = 1 / (ratio + 1)
pb = 1 - pg
n = 6
prob = 0
for i in range(3,7):
    combi = (m.factorial(n)) / ((m.factorial(i)) * (m.factorial(n - i)))
    p = combi * (pb**i) * (pg**(n - i))
    prob += p
print(round(prob, 3))
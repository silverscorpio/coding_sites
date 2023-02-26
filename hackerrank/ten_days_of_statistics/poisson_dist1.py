##### POISSON DISTRIBUTION - 1

import math as m

mean = float(input())
var = int(input())
prob = (((m.e) ** (-mean)) * (mean ** var)) / m.factorial(var)
print(round(prob, 3))
##### CENTRAL LIMIT THEOREM - 3

import math as m

samp_size = 100
pop_mean = 500
pop_stddev = 80
z = 1.96
a = pop_mean - (z * (pop_stddev / m.sqrt(samp_size)))
b = pop_mean + (z * (pop_stddev / m.sqrt(samp_size)))
print(round(a, 2))
print(round(b, 2))
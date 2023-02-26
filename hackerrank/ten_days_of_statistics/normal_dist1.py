##### NORMAL DISTRIBUTION - 1

import math as m
mean = 20
std_dev = 2
part_a = 19.5
part_b_lower = 20
part_b_upper = 22

cumu_prob = 0.5 * (1 + m.erf((part_a - mean) / (std_dev * m.sqrt(2))))

b_up = 0.5 * (1 + m.erf((part_b_upper - mean) / (std_dev * m.sqrt(2))))
b_low = 0.5 * (1 + m.erf((part_b_lower - mean) / (std_dev * m.sqrt(2))))

print(round(cumu_prob, 3))
print(round(b_up - b_low, 3))
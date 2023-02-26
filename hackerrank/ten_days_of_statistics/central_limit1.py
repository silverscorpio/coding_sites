##### CENTRAL LIMIT THEOREM - 1

import math as m

pop_mean = 205
pop_stddev = 15
n_boxes = 49
normal_mean = n_boxes * pop_mean
normal_stddev = m.sqrt(n_boxes) * pop_stddev

ans = (0.5 * (1 + m.erf((9800 - normal_mean) / (normal_stddev * m.sqrt(2)))))

print(round(ans, 4))
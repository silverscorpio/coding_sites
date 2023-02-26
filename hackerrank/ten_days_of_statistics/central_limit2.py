##### CENTRAL LIMIT THEOREM - 2

import math as m

no_students = 100
max_tickets = 250
tick_pop_mean = 2.4
tick_pop_stddev = 2.0

tick_norm_mean = tick_pop_mean * no_students
tick_norm_stddev = m.sqrt(no_students) * tick_pop_stddev

ans = 0.5 * (1 + m.erf((250 - tick_norm_mean) / (tick_norm_stddev * m.sqrt(2))))

print(round(ans, 4))
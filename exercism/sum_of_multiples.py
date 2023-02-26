### Exercise - 13 - Sum of multiples

import math as m

def sum_of_multiples(limit, multiples):
    mul_list = []
    for i in multiples:
        if i != 0:
            for j in range(1, m.ceil(limit / i)):
                if ((i * j) < limit) and ((i * j) not in mul_list):
                    mul_list.append(i * j)
        else:
            mul_list.append(0)
    return sum(mul_list)
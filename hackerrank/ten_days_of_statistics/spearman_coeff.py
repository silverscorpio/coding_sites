##### SPEARMAN'S RANK COEFFICIENT 

import math as m

def stddev(array_of_nums):
    numbs = array_of_nums
    numb_mean = sum(numbs) / len(numbs)
    el_diff = [(i - numb_mean) ** 2 for i in numbs]
    numerator = sum(el_diff)
    std_dev = m.sqrt(numerator / len(numbs))
    return std_dev

def mean(array_of_nums):
    return (sum(array_of_nums) / len(array_of_nums))

size = int(input())
x_input = input().split()
x = [float(i) for i in x_input]
y_input = input().split()
y = [float(i) for i in y_input]

mean_x = mean(x)
sd_x = stddev(x)
mean_y = mean(y)
sd_y = stddev(y)

sort_x = sorted(x)
sort_y = sorted(y)

rank_x = {x[i]:sort_x.index(x[i]) + 1 for i in range(len(x))}
rank_y = {y[i]:sort_y.index(y[i]) + 1 for i in range(len(y))}
di_sq = [((rank_x[x[i]] - rank_y[y[i]]) ** 2) for i in range(size)]

numer = 6 * sum(di_sq) 
deno = size * ((size ** 2) - 1)

spearman_coeff = 1 - (numer / deno)
print(round(spearman_coeff, 3))
##### PEARSON CORRELATION COEFFICIENT 1

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

numer = 0
for i in range(size):
    alpha = (x[i] - mean_x) * (y[i] - mean_y)
    numer += alpha
deno = size * sd_x * sd_y

pear_coeff = numer / deno
print(round(pear_coeff, 3))
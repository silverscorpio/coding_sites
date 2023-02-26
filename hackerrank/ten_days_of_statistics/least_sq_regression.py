##### LEAST SQUARE REGRESSION LINE

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

def pearson(x_array, y_array):
    size = len(x_array)
    x = x_array
    y = y_array
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
    return (round(pear_coeff, 3))
    
x_coord = [95, 85, 80, 70, 60]
y_coord = [85, 95, 70, 65, 70]

mean_x = mean(x_coord)
mean_y = mean(y_coord)
sd_x = stddev(x_coord)
sd_y = stddev(y_coord)
pear_coeff = pearson(x_coord, y_coord)
b = pear_coeff * (sd_y / sd_x)
a = mean_y - (b * mean_x)
ans = a + (b * 80)
print(round(ans, 3))
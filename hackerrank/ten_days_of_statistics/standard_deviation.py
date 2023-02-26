## STANDARD DEVIATION

import math

num_el = int(input())
numbs = input().split()
numbs = [int(i) for i in numbs]

numb_mean = sum(numbs) / len(numbs)
el_diff = [(i - numb_mean) ** 2 for i in numbs]
numerator = sum(el_diff)

std_dev = math.sqrt(numerator / len(numbs))
std_dev_rnd = round(std_dev, 1)
print(std_dev_rnd)
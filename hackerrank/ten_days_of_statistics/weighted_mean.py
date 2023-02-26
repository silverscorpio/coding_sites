## WEIGHTED MEAN

num_el = int(input())
numby = input().split()
numby = [int(i) for i in numby]
weights = input().split()
weights = [int(i) for i in weights]
sumy = 0
for i in range(len(numby)):
    sumy += numby[i] * weights[i]

weight_mean = round((sumy / sum(weights)), 1)
print(weight_mean)
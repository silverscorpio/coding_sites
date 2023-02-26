##### GEOMETRIC DISTRIBUTION - 2

# defect = success
vals = input().split()
inspect = int(input())
pd = float(vals[0]) / float(vals[1])
prob = 0
for i in range(0, inspect):
    x = ((1 - pd) ** i) * (pd)
    prob += x
print(round(prob, 3))
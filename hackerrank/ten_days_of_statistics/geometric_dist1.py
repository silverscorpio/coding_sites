##### GEOMETRIC DISTRIBUTION - 1

# defect = success
vals = input().split()
inspect = int(input())
pd = float(vals[0]) / float(vals[1])
prob = ((1 - pd) ** (inspect - 1)) * (pd)
print(round(prob, 3))

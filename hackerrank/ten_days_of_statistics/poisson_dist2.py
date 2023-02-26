##### POISSON DISTRIBUTION - 2

means = input().split()
mean_A = float(means[0])
mean_B = float(means[1])
mach_A_cost = 160 + 40 * (mean_A + ((mean_A) ** 2))
mach_B_cost = 128 + 40 * (mean_B + ((mean_B) ** 2))
print(round(mach_A_cost, 3))
print(round(mach_B_cost, 3))
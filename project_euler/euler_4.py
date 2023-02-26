# Problem 4

def str_rev(a):
    check = []
    for i in range(0, len(a)):
        alpha = a[-1* (i + 1)]
        check.append(alpha)
    return ''.join(check)

combi = []
for i in range(100, 1000):
    for j in range(100, 1000):
        combi.append(i * j)
palins = []
for alpha in combi:
    if str(alpha) == str_rev(str(alpha)):
        palins.append(alpha)
    else:
        pass
print(max(palins))


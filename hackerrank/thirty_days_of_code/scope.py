# Scope question

a = [1,2,5]
diff = 0

p = 0
q = 1
while p != len(a) - 1:
    for i in range(q, len(a)):
        ab_diff = abs(a[p] - a[i])
        if ab_diff > diff:
            diff = ab_diff
        else:
            pass
    p += 1
    q += 1
print(diff)
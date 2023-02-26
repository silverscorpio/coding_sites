# Maximum no of consecutive 1s in the binary form of a number

a = bin(int(input()))
b = a[2:]
c = ['1' * i for i in range(1, len(b) + 1)]
ans = 0
for j in c:
    if j in b:
        ans = j
    else:
        pass
print(f"Max no. of consecutive 1s: {len(ans)}")
print(f"Binary form: {b}")
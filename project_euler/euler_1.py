# Problem 1

a = int(input())
ans = []
i = 1
while i < a:
    if i % 3 ==0 or i % 5 == 0:
        ans.append(i)
        i += 1
    else:
        pass
        i += 1
print(sum(ans))
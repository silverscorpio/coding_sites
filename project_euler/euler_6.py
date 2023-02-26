# Problem 6

def ans(n):
    a = []
    b = []
    for i in range(1, n+1):
        a.append(i**2)
        b.append(i)
    alpha = sum(a)
    beta = (sum(b)) ** 2
    req = alpha - beta
    return abs(req)

x = ans(100)
print(x)
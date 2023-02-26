# Problem 2

def fibo_sumeven():
    a = 1
    b = 2
    terms = [a, b]
    i = 0
    addy = 0
    check = True
    while check:
        addy = terms[i] + terms[i + 1]
        if addy < 4000000:
            terms.append(addy)
            i += 1
            check = True
        elif addy >= 4000000:
            check = False
    alpha = []
    for i in terms:
        if i % 2 ==0:
            alpha.append(i)
        else:
            pass
    return sum(alpha)
x = fibo_sumeven()
print(x)
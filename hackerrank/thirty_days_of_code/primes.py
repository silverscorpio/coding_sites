### Prime Number

import math
def prime_test(a):  # a > 1
    if a != 2 and a % 2 == 0:
        return "Not prime"
    elif a == 1:
        return "Not prime"
    elif a == 2 or a % 2 != 0:
        i = 2
        count = 0
        if a == i:
            return "Prime"
        elif a != i:
            while i <= math.ceil(math.sqrt(a)):
                if a % i != 0:
                    i += 1
                elif a % i == 0:
                    count = 1
                    break
            if count == 0:
                return "Prime"
            elif count > 0:
                return "Not prime"

def no_primes(b):   # b > 0
    primes= []
    if b == 1:
        return primes
    elif b == 2:
        primes.append(b)
        return primes
    elif b > 2:
        primes.append(2)
        j = 3
        while j <= b:
            alpha = prime_test(j)
            if alpha == 'Prime':
                primes.append(j)
                j += 1
            elif alpha == 'Not prime':
                j += 1
    return primes

a = int(input())
i = 0
numbers = []
while i < a:
    num = int(input())
    numbers.append(num)
    i += 1

for j in numbers:
    if len(str(j)) <= 9:
        x = prime_test(j)
        print(x)
    elif len(str(j)) > 9:
        if j % 2 == 0 or j % 10 == 5:
            print("Not prime")
        else:
            limit = math.ceil(math.sqrt(j))
            listy = no_primes(limit)
            check = 0
            for i in listy:
                if j % i != 0:
                    pass
                elif j % i == 0:
                    check = 1
                    break
            if check == 0:
                print("Prime")
            else:
                print("Not prime")
    
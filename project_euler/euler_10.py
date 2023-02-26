# Problem 10

import prime_test from euler_3

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
            if alpha == 'prime':
                primes.append(j)
                j += 1
            elif alpha == 'not prime':
                j += 1
    return primes

main1 = [i for i in range(1, 2000000, 2) if (i % 10 != 5 or i == 5)]
listy = no_primes(20000) # with 20000 time=54 sec, with 40000, time=1.44 min
for k in listy:
    main1 = [i for i in main1 if (i % k != 0 or i == k)]
main1.remove(1)
main1.insert(0,2)
# print(main1[0:30])
print(len(main1))
print(sum(main1))

# Problem 7

import prime_test from euler_3

n = int(input("Number: "))
count_prime = 0
that_prime = 0
i = 2
while count_prime != n:
    if prime_test(i) == 'prime':
        that_prime = i
        count_prime += 1
        i += 1
    else:
        i += 1
print(that_prime)
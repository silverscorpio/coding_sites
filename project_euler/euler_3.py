# Problem 3

def prime_test(a):  # a > 1
    if a != 2 and a % 2 == 0:
        return "not prime"
    elif a == 2 or a % 2 != 0:
        i = 2
        count = 0
        if a == i:
            return "prime"
        elif a != i:
            while i < a:
                if a % i != 0:
                    count += 1
                    i += 1
                elif a % i == 0:
                    count = 0
                    break
            if count == 0:
                return "not prime"
            elif count > 0:
                return "prime"
            
d = int(input("Number: "))
divisor = 2
dividend = d
while dividend >= divisor:
    check = prime_test(divisor)
    if check == 'prime' and dividend % divisor == 0:
        condi = True
        while condi:
            div = dividend // divisor
            dividend = div
            if dividend % divisor == 0:
                continue
            elif dividend % divisor != 0 and dividend != 1:
                divisor += 1
                condi = False
            elif dividend == 1:
                condi = False
    elif check == 'prime' and dividend % divisor != 0:
        divisor += 1
    elif check == 'not prime':
        divisor += 1
print(f"Greatest Prime Divisor: {divisor}")
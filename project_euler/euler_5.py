# Problem 5

import prime_test from euler_3

def prime_fact(d):
    divisor = 2
    dividend = d
    divs_req = []
    while dividend >= divisor:
        check = prime_test(divisor)
        if check == 'prime' and dividend % divisor == 0:
            condi = True
            while condi:
                div = dividend // divisor
                dividend = div
                divs_req.append(divisor)
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
    return divs_req
    print(f"Greatest Prime Divisor: {divisor}")
    print(f"Prime Factorization: {divs_req}")



# LCM
def lcm_nos(a):  # a is a list of the numbers
    fact = []
    fact_set = []
    common_count = {}
    common_min = {}
    final = 1
    for i in range(0, len(a)):
        fact.append(prime_fact(a[i]))
        fact_set.append(set(prime_fact(a[i])))
    for j in range(1, len(fact_set)):
        fact_set[0] = fact_set[0].union(fact_set[j])
    for alpha in fact_set[0]:
        common_count[str(alpha)+"s"] = []
        for beta in fact:
            common_count[str(alpha)+"s"].append(beta.count(alpha))
    for k in fact_set[0]:
        common_min["min_"+str(k)+"s"] = max(common_count[str(k)+"s"])
        if common_min["min_"+str(k)+"s"] != 0:
            final *= k ** common_min["min_"+str(k)+"s"]
        else:
            pass
    return final
x= lcm_nos(list(range(1,20)))
print(x)

# HCF not asked in Euler 5 but noted here for completeness of HCF & LCM stuff
# Extra

def hcf_nos(a):  # a is a list of the numbers
    fact = []
    fact_set = []
    common_count = {}
    common_min = {}
    final = 1
    for i in range(0, len(a)):
        fact.append(prime_fact(a[i]))
        fact_set.append(set(prime_fact(a[i])))
    for j in range(1, len(fact_set)):
        fact_set[0] = fact_set[0].union(fact_set[j])
    for alpha in fact_set[0]:
        common_count[str(alpha)+"s"] = []
        # common_min["min_"+str(alpha)+"s"] = []
        for beta in fact:
            common_count[str(alpha)+"s"].append(beta.count(alpha))
            # common_min["min_"+str(alpha)+"s"].append(min(common_count[str(alpha)+"s"]))
    for k in fact_set[0]:
        common_min["min_"+str(k)+"s"] = min(common_count[str(k)+"s"])
        if common_min["min_"+str(k)+"s"] != 0:
            final *= k ** common_min["min_"+str(k)+"s"]
        else:
            pass
    return final
x= hcf_nos([8, 12, 20])
print(x)
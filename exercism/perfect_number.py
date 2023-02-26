### Exercise - 25 - Perfect, Abundant or deficient

def sum_prop_fact(n):
    facts = []
    count = 0
    for i in range(1, n):
        if n % i == 0:
            facts.append(i)
            count += 1
    return sum(facts)


def classify(number):
    if number == 0 or number == -1:
        raise ValueError("Invalid Input")
    else:
        sum_facts = sum_prop_fact(number)
        if sum_facts == number:
            return "perfect"
        elif sum_facts > number:
            return 'abundant'
        elif sum_facts < number:
            return 'deficient'
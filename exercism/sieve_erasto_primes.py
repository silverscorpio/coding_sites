### Exercise - 24 - Sieve - Good!! Finally!!

def primes(limit):
    if limit == 1:
        return []
    else:
        listy = set(range(2, limit + 1))
        p = 2
        while p != limit:
            to_be_removed = set(range(2 * p, limit + 1, p))
            removal = listy.difference(to_be_removed)
            listy = removal
            p += 1
        return (sorted(list(listy)))
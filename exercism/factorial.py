# factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        while n != 1:
            alpha = 1
            alpha *= n * factorial(n - 1)
            n -= 1
            return alpha
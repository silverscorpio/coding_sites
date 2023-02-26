### Exercise - 10 - Difference of Squares

def square_of_sum(number):
    n = number
    sum_sq = ((n * (n + 1)) // 2) ** 2
    return sum_sq


def sum_of_squares(number):
    n = number
    sq = [i ** 2 for i in range(n + 1)]
    return sum(sq)


def difference_of_squares(number):
    alpha = square_of_sum(number)
    beta = sum_of_squares(number)
    return alpha - beta
### Exercise - 12 - String Reversal

def reverse(text):
    a = text
    check = []
    beta = ''
    for i in range(0, len(a)):
        alpha = a[-1 * (i + 1)]
        check.append(alpha)
    return beta.join(check)
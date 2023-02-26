### Exercise - 2 - TWO FER

def two_fer(*X):
    if len(X) != 0:
        return (f"One for {X[0]}, one for me.")
    else:
        return ("One for you, one for me.")
### Exercise - 4 - HIGH SCORES

def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    a = scores
    ans = []
    if len(a) > 3:
        i = 0
        while i < 3:
            s = max(a)
            ans.append(s)
            a.remove(s)
            i += 1
        return ans

    elif len(a) <= 3:
        b = sorted(a, reverse = True)
        return b
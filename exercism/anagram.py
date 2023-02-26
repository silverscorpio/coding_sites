# anagrams

import random

def find_anagrams(word, candidates):
    case = {}
    for alpha in candidates:
        case[alpha.lower()] = alpha
    mod_cand = [i.lower() for i in candidates if len(i) == len(word)]
    word_itself = list(word.lower())
    word_itself1 = sorted(word_itself)
    mod_cand1 = []
    for x in mod_cand:
        y = sorted(list(x.lower()))
        if (y == word_itself1):
            if (x != word.lower()):
                mod_cand1.append(x)
    available = []
    if mod_cand1 == []:
        return available
    else:
        used = []
        repeats = {}
        for j in word_itself:
            counter = word_itself.count(j)
            if counter > 1:
                repeats[j] = counter
        limit = factorial(len(word))
        for k in repeats.values():
            limit = limit // factorial(k)
        limit -= 1
        while len(used) != limit:
            b = list(word.lower())
            c = random.sample(b, len(word))
            d = ''.join(c)
            if d != word and d not in used:
                used.append(d)
                for k in mod_cand1:
                    if k == d:
                        available.append(case[k])
                if len(available) == len(mod_cand1):
                    break
        return available
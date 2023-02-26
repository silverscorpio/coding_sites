### Exercise - 7 - ISOGRAM

import string as s

def is_isogram(string):

    alpha_set = list(s.ascii_lowercase)
    alpha_set.append(' ')
    alpha_set.append('-')

    count = 0
    word = string.lower()
    for i in alpha_set:
        if i not in [' ', '-']:
            if word.count(i) > 1:
                count = 1
        elif i in [' ', '-']:
            if word.count(i) > 1:
                pass

    if count == 1:
        return False
    elif count == 0:
        return True
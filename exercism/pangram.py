### Exercise - 16 - Pangram

import string


def is_pangram(sentence):
    alpha_set = string.ascii_lowercase
    non_alpha_set = ['-', " ' ", '_', '.', ' " ']
    used_alpha = []
    sent_split = sentence.split()
    combi_sent = (''.join(sent_split)).lower()
    for k in alpha_set:
        if (k in combi_sent) and (k not in used_alpha) and (k not in non_alpha_set):
            used_alpha.append(k)
    return True if len(used_alpha) == 26 else False
### SWAP CASE

import string
def swap_case(s):
    z = []
    y = s.split()
    for i in y:
        x = []
        for j in i:
            if (j in string.ascii_lowercase) or (j in string.ascii_uppercase):
                if j.islower():
                    k = j.upper()
                elif j.isupper():
                    k = j.lower()
            else:
                k = j
            x.append(k)
        z.append(''.join(x))
    return ' '.join(z)

s = 'HackerRank.com presents "Pythonist 2".'
c = 'hACKERrANK.COM PRESENTS "pYTHONIST 2".'
print(swap_case(s) == c)
# HackerRank.com presents "Pythonist 2".
# hACKERrANK.COM PRESENTS "pYTHONIST 2".
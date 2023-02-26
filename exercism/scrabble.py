### Exercise - 8 - SCRABBLE

# A, E, I, O, U, L, N, R, S, T       1
# D, G                               2
# B, C, M, P                         3
# F, H, V, W, Y                      4
# K                                  5
# J, X                               8
# Q, Z                               10

def score(word):
    set_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T', '1']
    set_2 = ['D', 'G', '2']
    set_3 = ['B', 'C', 'M', 'P', '3']
    set_4 = ['F', 'H', 'V', 'W', 'Y', '4']
    set_5 = ['K', '5']
    set_6 = ['J', 'X', '8']
    set_7 = ['Q', 'Z', '10']
    set_all = [set_1, set_2, set_3, set_4, set_5, set_6, set_7]
    points = {}
    i = 0
    while i < 7:
        for j in set_all:
            for k in j[:-1]:
                points.update({k: int(j[-1])})
        i += 1
    score = 0
    the_word = word.upper()
    for x in the_word:
        score += points[x]
    return score
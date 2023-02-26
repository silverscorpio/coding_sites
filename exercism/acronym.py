### Exercise - 9 - ACRONYM

def abbreviate(words):
    delimits = ['_', '-']
    first_letters = []
    wordies = words.split()

    for i in delimits:
        while wordies.count(i) != 0:
            wordies.remove(i)
        for j in wordies:
            if i in j:
                if (j[0] == i) or (j[-1] == i):
                    position = wordies.index(j)
                    wordies.remove(j)
                    new = j.strip(i)
                    wordies.insert(position, new)
                else:
                    position = wordies.index(j)
                    wordies.remove(j)
                    j = j.split(i)
                    for k in range(len(j) - 1, -1, -1):
                        wordies.insert(position, j[k])
    for i in wordies:
        first_letters.append(i[0].upper())
    abb = ''.join(first_letters)
    return abb
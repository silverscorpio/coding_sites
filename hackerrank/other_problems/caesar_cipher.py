# caesar cipher

import string
from time import sleep


# start >= 1
def cycler(text: str, start: int, cycles: int):
    counter, indexer = 0, start - 1
    while counter != abs(cycles) + 1:
        if cycles > 0:
            if indexer == len(text):
                indexer = 0
            indexer += 1
        elif cycles < 0:
            if indexer == -1:
                indexer = len(text) - 1
            indexer -= 1
        # print(text[indexer], indexer, counter)
        counter += 1
        # sleep(0.1)

        # to get the final character
        # print(text[indexer - 1])
    return text[indexer - 1] if cycles > 0 else text[indexer + 1]

    # else:
    # 1st method
    # indexer = start * - 1
    # while counter != abs(cycles) + 1:
    #     if abs(indexer) == len(text) + 1:
    #         indexer = -1
    #     # print(text[indexer], indexer, counter)
    #     indexer += 1
    #     counter += 1
    #     # sleep(0.2)
    #
    # # to get the final character
    # # print(text[indexer - 1])
    # return text[indexer + 1]

    # 2nd method
    # while counter != abs(cycles) + 1:
    #     if indexer == -1:
    #         indexer = len(text) - 1
    #     # print(text[indexer], indexer, counter)
    #     indexer -= 1
    #     counter += 1
    #     # sleep(0.2)
    #
    # # to get the final character
    # return text[indexer + 1]
    # # print(text[indexer - 1])


# print(cycler("panda", 3, -6))


def encrypt(text: str, cycles: int) -> str:
    encryption = []
    for char_index, char in enumerate(text):
        if char.isalpha():
            if char.islower():
                encryption.append(cycler(string.ascii_lowercase, string.ascii_lowercase.index(char) + 1, cycles))
            elif char.isupper():
                encryption.append(
                    cycler(string.ascii_lowercase, string.ascii_lowercase.index(char.lower()) + 1, cycles).upper())
        else:
            encryption.append(char)

    return ''.join(encryption)


# string_to_encrypt = 'The cat sat on the mat'
string_to_encrypt = "Esp nle dle zy esp xle"
# rotations = 11
rotations = -11
print(encrypt(string_to_encrypt, rotations))
# print(encrypt('panda', 1))
# print(encrypt("qboeb", -1))

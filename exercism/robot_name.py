## Exercise - 15 - Robot name - Good!

import random as r
import string as s

used_seeds = []


def gen_name():
    seed = r.random()
    while seed in used_seeds != False:
        seed = r.random()
    used_seeds.append(seed)
    alpha_set = list(s.ascii_uppercase)
    all_chars = []
    counter = 0
    dig_len = 3
    alpha_len = 2
    while counter < alpha_len:
        all_chars.append(r.choice(alpha_set))
        counter += 1

    counter = 0

    while counter < dig_len:
        all_chars.append(str(r.randint(0, 9)))
        counter += 1
    name = ''.join(all_chars)
    return name


class Robot:

    def __init__(self):
        self.name = gen_name()

    def reset(self):
        self.name = ''
        self.name = gen_name()
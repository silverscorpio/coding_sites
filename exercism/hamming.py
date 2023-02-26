### Exercise - 6 - HAMMING 

def distance(strand_a, strand_b):
    if len(strand_a) == 0 and len(strand_b) == 0:
        return 0

    elif len(strand_a) == 0 or len(strand_b) == 0:
        if len(strand_a) == 0:
            raise ValueError("Left strand empty")
        else:
            raise ValueError("Right strand empty")

    elif len(strand_a) != len(strand_b):
        if len(strand_a) > len(strand_b):
            raise ValueError("Left strand longer")
        elif len(strand_a) < len(strand_b):
            raise ValueError("Right strand longer")

    else:
        count = 0
        for i in range(len(strand_a)):
            check = strand_a[i] == strand_b[i]
            if not check:
                count += 1
            else:
                pass
        return count
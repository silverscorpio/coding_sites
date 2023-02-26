### Exercise - 14 - Armstrong Number

def is_armstrong_number(number):
    num_str = str(number)
    len_num_str = len(num_str)
    sumy = 0
    for i in num_str:
        sumy += (int(i) ** len_num_str)
    return True if (sumy == number) else False

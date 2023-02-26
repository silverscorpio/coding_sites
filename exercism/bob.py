### Exercise - 23 - Bob

import string

def response(hey_bob):
    ques = hey_bob

    check1 = 0
    check_set1 = list(string.ascii_lowercase)
    for i in ques:
        if i in check_set1:
            check1 = 1
            break
    check2 = 0
    check_set2 = [str(i) for i in range(0, 10)]
    for i in ques:
        if i in check_set2:
            check2 = 1
            break
    if '?' in ques and ques.count('?') == 1 and ques.isupper() != True:
        if ques.strip()[-1] == '?':
            return 'Sure.'
        else:
            return 'Whatever.'
    elif ques.isupper() == True and ques[-1] != '?':
        return 'Whoa, chill out!'
    elif ques.isupper() == True and ques[-1] == '?':
        return "Calm down, I know what I'm doing!"
    elif (check1 == 0) and ((ques.count("\t") >= 1) or (ques.count("\n") >= 1) or (ques.count(" ") >= 0)) and (check2 == 0):
        return 'Fine. Be that way!'
    else:
        return "Whatever."
### NUMBER OF TIMES SUB STRING OCCURS IN STRING

def count_substring(string, sub_string):
    count = 0
    # l = [sub_string]
    p = 0
    q = len(sub_string)
    while q != len(string) + 1:
        if string[p:q] == sub_string:
            count += 1
        p += 1
        q += 1
    return count

print(count_substring('ABCDCDC', 'CDC'))
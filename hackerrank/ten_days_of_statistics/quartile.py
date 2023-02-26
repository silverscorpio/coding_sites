##### QUARTILE

def median(numbs):
    numb_sort = sorted(numbs)
    if len(numb_sort) % 2 == 0:
        median = (numb_sort[(len(numb_sort) // 2) - 1] + numb_sort[((len(numb_sort) // 2) + 1) - 1]) / 2
        median = round(median, 1)
    else:
        median = numb_sort[((len(numb_sort) + 1) // 2) - 1]
        median = round(median, 1)
        
    return median 
    
# Main
numby = int(input())
numbers = input().split()
numbers = [int(i) for i in numbers]
numbers_sort = sorted(numbers)

if len(numbers_sort) % 2 == 0:
    q2 = median(numbers)
    left_half = numbers_sort[:(len(numbers_sort) // 2)]
    right_half = numbers_sort[(len(numbers_sort) // 2):]
    q1 = median(left_half)
    q3 = median(right_half)
else:
    q2 = median(numbers)
    left_half = numbers_sort[:numbers_sort.index(q2)]
    right_half = numbers_sort[numbers_sort.index(q2) + 1:]
    q1 = median(left_half)
    q3 = median(right_half)
    
print(int(q1))
print(int(q2))
print(int(q3))
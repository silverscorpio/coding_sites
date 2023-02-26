##### INTERQUARTILE RANGE WITH FREQUENCY DATA

def median(numbs):
    numb_sort = sorted(numbs)
    if len(numb_sort) % 2 == 0:
        median = (numb_sort[(len(numb_sort) // 2) - 1] + numb_sort[((len(numb_sort) // 2) + 1) - 1]) / 2
    else:
        median = numb_sort[((len(numb_sort) + 1) // 2) - 1]

    return median 
    

def quartile(numbers):
    numbers_sort = sorted(numbers)
    if len(numbers_sort) % 2 == 0:
        q2 = median(numbers)
        left_half = numbers_sort[:(len(numbers_sort) // 2)]
        right_half = numbers_sort[(len(numbers_sort) // 2):]
        q1 = median(left_half)
        q3 = median(right_half)
    else:
        q2 = median(numbers)
        left_half = numbers_sort[:((len(numbers_sort) + 1) // 2) - 1]
        right_half = numbers_sort[((len(numbers_sort) + 1) // 2):]
        q1 = median(left_half)
        q3 = median(right_half)
        
    return q1, q2, q3
    
# Main
numby = int(input())

X = input().split()
X = [[int(i)] for i in X]

F = input().split()
F = [int(i) for i in F]

numbers = [X[i] * F[i] for i in range(len(X))]
numbers1 = []
for i in numbers:
    for j in i:
        numbers1.append(j)

Q1, Q2, Q3 = quartile(numbers1)
print(round(float(Q3 - Q1), 1))

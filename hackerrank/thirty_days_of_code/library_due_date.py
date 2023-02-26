# Library - Due Date

act = input().split()
expect = input().split()

actual = [int(i) for i in act]
expected = [int(i) for i in expect]
fine = -1

if (actual[1] == expected[1]) and (actual[2] == expected[2]):
    if actual[0] <= expected[0]:
        fine = 0
    elif actual[0] > expected[0]:
        fine = 15 * (actual[0] - expected[0])
elif (actual[1] < expected[1]) and (actual[2] == expected[2]):
    fine = 0
elif (actual[1] > expected[1]) and (actual[2] == expected[2]):
    fine  = 500 * (actual[1] - expected[1])
elif actual[2] > expected[2]:
    fine = 10000
elif actual[2] < expected[2]:
    fine = 0

print(fine)
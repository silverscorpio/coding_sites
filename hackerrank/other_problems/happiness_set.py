### HAPPINESS SET

# VERSION 1 - SLOW!!
i = 0
inputs = []
while i != 4:
    s = input().split()
    inputs.append(s)
    i += 1

sizes = [int(i) for i in inputs[0]]
nums = [int(i) for i in inputs[1]]
arrayA = [int(i) for i in inputs[2]]
arrayB = [int(i) for i in inputs[3]]

happy = 0
for i in nums:
    if i in arrayA:
        happy += 1
    elif i in arrayB:
        happy -= 1

print(happy)

# VERSION 2
i = 0
inputs = []
while i != 4:
    s = input().split()
    inputs.append(s)
    i += 1

# nums = [int(i) for i in inputs[1]]
# arrayA = [int(i) for i in inputs[2]]
# arrayB = [int(i) for i in inputs[3]]

nums = set(inputs[1])
x = []
arrayA = [int(i) for i in inputs[2]]
arrayB = [int(i) for i in inputs[3]]

happy = 0
for i in nums:
    if int(i) in arrayA:
        happy += 1
    elif int(i) in arrayB:
        happy -= 1

print(happy)

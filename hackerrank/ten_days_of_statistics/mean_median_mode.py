## MEAN, MEDIAN, MODE

numby = int(input())
numbers = input().split()
numbers = [int(i) for i in numbers]

# mean
mean = round((sum(numbers) / len(numbers)), 1)

# median
numb_sort = sorted(numbers)
if len(numb_sort) % 2 == 0:
    median = (numb_sort[(len(numb_sort) // 2) - 1] + numb_sort[((len(numb_sort) // 2) + 1) - 1]) / 2
    median = round(median, 1)
else:
    median = numb_sort[((len(numb_sort) + 1) // 2) - 1]
    median = round(median, 1)
  
# mode
numb_counts = {i:numbers.count(i) for i in numbers}
max_numb, max_count = 0, 0
for numby, counts in numb_counts.items():
    if counts > max_count:
        max_count, max_numb = counts, numby
    elif (counts == max_count) and (numby < max_numb):
        max_count, max_numb = counts, numby

mode = max_numb

print(f"""
{mean}
{median}
{mode}
""")

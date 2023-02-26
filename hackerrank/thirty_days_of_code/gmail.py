### Gmail

# 6
# riya riya@gmail.com
# julia julia@julia.me
# julia sjulia@gmail.com
# julia julia@gmail.com
# samantha samantha@gmail.com
# tanya tanya@gmail.com

a = int(input())
i = 0
names = []
emails = []
while i < a:
    stuff = input().split()
    names.append(stuff[0])
    emails.append(stuff[1])
    i += 1
ans = []
for i in range(len(emails)):
    if '@gmail.com' in emails[i]:
        listy = [names[i], emails[i]]
        ans.append(listy)
    else:
        pass
req_names = [i[0] for i in ans]
req_names.sort()
for i in req_names:
    print(i)
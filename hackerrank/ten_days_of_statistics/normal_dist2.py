##### NORMAL DISTRIBUTION - 2


import math as m
mean = 70
std_dev = 10
higher_than_80 = 80
passed = 60
failed = 60
ans1 = 1 - (0.5 * (1 + m.erf((higher_than_80 - mean) / (std_dev * m.sqrt(2)))))
ans2 = 1 - (0.5 * (1 + m.erf((passed - mean) / (std_dev * m.sqrt(2)))))
ans3 = 0.5 * (1 + m.erf((failed - mean) / (std_dev * m.sqrt(2))))

ans = [ans1, ans2, ans3]
for i in ans:
    print(round(i * 100, 2))
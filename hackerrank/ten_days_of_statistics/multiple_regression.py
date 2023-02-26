##### MULTIPLE LINEAR REGRESSION

import numpy as np

vals = input().split()
m = int(vals[0])
n = int(vals[1])
features = []
y_vals = []
i = 0
while i < n:
    a = input().split()
    charlie = [ float(a[q]) for q in range(len(a) - 1) ]
    charlie.insert(0, 1)
    features.append(charlie)
    y_vals.append(float(a[-1]))
    i += 1
i = 0
q = int(input())
test_features = []
while i < q:
    a = input().split()
    delta = [ float(p) for p in a ]
    delta.insert(0, 1)
    test_features.append(delta)
    i += 1
    
# Y = X * B
Y = (np.array(y_vals)).reshape(len(y_vals), 1)
X = np.array(features)
B1 = np.linalg.inv(np.matmul(np.transpose(X), X))
B2 = np.transpose(X)
B = np.matmul(np.matmul(B1, B2), Y)
a = B[0, 0]
b1 = B[1,0]
b2 = B[2, 0]

# y = a + b1 * x1 + b2 * x2
ans = [np.matmul(j, B) for j in test_features]
for k in ans:
    print(round(k[0],3))

N, M = map(int, input().split())

A = list(map(int, input().split()))
X = []
for _ in range(N):
    row = list(map(int, input().split()))
    X.append(row)

flag = 1

for i in range(M):
    X_m = 0
    for j in range(N):
        X_m += X[j][i]
    if X_m < A[i]:
        flag = 0
        break

if flag == 1:
    print("Yes")
else:
    print("No")

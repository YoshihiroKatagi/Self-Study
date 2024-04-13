N = int(input())
p = list()
for i in range(N):
    x = list(map(int,input().split()))
    p.append(x)

ans = list()

for i in range(N):
    x1 = p[i][0]
    y1 = p[i][1]
    ans_d = 0
    ans_j = 0
    for j in range(N):
        if i == j:
            continue

        x2 = p[j][0]
        y2 = p[j][1]

        d = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)
        if d > ans_d:
            ans_d = d
            ans_j = j + 1
    ans.append(ans_j)

for i in range(N):
    print(ans[i])


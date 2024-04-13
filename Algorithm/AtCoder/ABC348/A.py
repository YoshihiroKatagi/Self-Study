N = int(input())

ans = ""
for i in range(N):
    if (i + 1) % 3 == 0:
        ans += "x"
    else:
        ans += "o"

print(ans)
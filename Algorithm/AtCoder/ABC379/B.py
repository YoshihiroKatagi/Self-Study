N, K = map(int, input().split())
S = input()

ans = 0
count = 0
for i in range(len(S)):
  teeth = S[i]
  if teeth == "O":
    count += 1
  else:
    count = 0
  if count == K:
    ans += 1
    count = 0

print(ans)
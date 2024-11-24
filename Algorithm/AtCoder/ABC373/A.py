S = [input() for i in range(12)]
ans = 0
# print(S)
for i in range(12):
  if len(S[i]) == i + 1:
    ans += 1

print(ans)
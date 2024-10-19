N, C = map(int, input().split())
T = list(map(int, input().split()))

# print(T)
prev = 0
ans = 0
for i in range(N):
  cur = T[i]
  if i == 0:
    ans += 1
    prev = T[i]
    continue
  # print("---")
  # print(prev)
  # print(cur)
  # print("---")

  if cur - prev >= C:
    ans += 1
    prev = T[i]

print(ans)

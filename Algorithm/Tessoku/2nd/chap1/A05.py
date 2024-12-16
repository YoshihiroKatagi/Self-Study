N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
  for j in range(1, N+1):
    z = K - i - j
    if z >= 1 and z <= N:
      ans += 1

print(ans)
def GetScore(a, b, A, B, N, K):
  cnt = 0
  for i in range(N):
    if a<=A[i] and A[i]<=a+K and b<=B[i] and B[i]<=b+K:
      cnt += 1
  return cnt

N, K = map(int, input().split())
A = [ None ] * N
B = [ None ] * N
for i in range(N):
  A[i], B[i] = map(int, input().split())

ans = 0
for a in range(1, 101):
  for b in range(1, 101):
    score = GetScore(a, b, A, B, N, K)
    ans = max(ans, score)

print(ans)
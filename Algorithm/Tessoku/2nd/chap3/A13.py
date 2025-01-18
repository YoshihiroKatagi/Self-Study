N, K = map(int, input().split())
A = list(map(int, input().split()))

R = [ None ] * N
for i in range(N):
  if i == 0:
    R[i] = 1
  else:
    R[i] = R[i-1]

  while R[i] < N and A[R[i]] - A[i] <= K:
    R[i] += 1

ans = 0
for i in range(N):
  ans += R[i] - (i+1)

print(ans)
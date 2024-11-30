import bisect

N = int(input())
A = list(map(int, input().split()))

dp = [ None ] * (N)
L = []
LEN = 0

for i in range(N):
  pos = bisect.bisect_left(L, A[i])
  dp[i] = pos

  if dp[i] >= LEN:
    L.append(A[i])
    LEN += 1
  else:
    L[dp[i]] = A[i]

print(LEN)
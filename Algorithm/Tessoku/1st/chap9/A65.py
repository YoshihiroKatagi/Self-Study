N = int(input())
A = list(map(int, input().split()))

G = [ list() for i in range(N+1) ]
dp = [0] * (N+1)

for i in range(N-1):
  G[A[i]].append(i+2)

for i in range(N, 0, -1):
  # dp[i] = 0
  for j in range(len(G[i])):
    dp[i] += (dp[G[i][j]]+1)
  
for i in range(1, N+1):
  if (i >= 2):
    print(" ", end="")
  print(dp[i], end="")

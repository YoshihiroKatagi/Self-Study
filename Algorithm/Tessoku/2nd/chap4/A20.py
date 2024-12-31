S = input()
T = input()

N = len(S)
M = len(T)

dp = [ [ None ] * (M + 1) for i in range(N + 1) ]

dp[0][0] = 0
for i in range(1, M+1):
  dp[0][i] = 0

for i in range(1, N+1):
  for j in range(M+1):
    if j == 0:
      dp[i][j] = 0
    else:
      if S[i-1] == T[j-1]:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])
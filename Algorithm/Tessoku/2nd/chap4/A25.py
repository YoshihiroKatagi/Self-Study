H, W = map(int, input().split())

c = [ None ] * H

for i in range(H):
  c[i] = input()

dp = [ [ 0 ] * W for i in range(H) ]

for i in range(H):
  for j in range(W):
    if i == 0 and j == 0:
      dp[i][j] = 1
    else:
      dp[i][j] = 0
      if i >= 1 and c[i-1][j] == '.':
        dp[i][j] += dp[i-1][j]
      if j >= 1 and c[i][j-1] == '.':
        dp[i][j] += dp[i][j-1]

print(dp[H-1][W-1])
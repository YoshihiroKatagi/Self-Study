N, A, B = map(int, input().split())

dp = [ None ] * (N+1)
dp[0] = False
# for i in range(A):
#   dp[i] = False

for i in range(1, N+1):
  if i < A:
    dp[i] = False
  else:
    if dp[i-A] == False or dp[i-B] == False:
      dp[i] = True
    else:
      dp[i] = False

if dp[N] == True:
  print("First")
else:
  print("Second")
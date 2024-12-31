N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [ -(10 ** 9) ] * (N+1)

dp[1] = 0

for i in range(N-1):
  dp[A[i]] = max(dp[A[i]], dp[i+1]+100)
  dp[B[i]] = max(dp[B[i]], dp[i+1]+150)

print(dp[N])
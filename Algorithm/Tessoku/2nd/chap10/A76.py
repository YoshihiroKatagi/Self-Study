import bisect

N, W, L, R = map(int, input().split())
X = list(map(int, input().split()))

X = [0] + X + [W]

MOD = 10**9 + 7
dp = [ None ] * (N + 2)
dpsum = [ None ] * (N + 2)
dp[0] = 1
dpsum[0] = 1

for i in range(1, N + 2):
  posl = bisect.bisect_left(X, X[i] - R)
  posr = bisect.bisect_right(X, X[i] - L + 1) - 1
  dp[i] = (dpsum[posr] if posr >= 0 else 0) - (dpsum[posl - 1] if posl > 0 else 0)
  dp[i] %= MOD
  dpsum[i] = dpsum[i - 1] + dp[i]
  dpsum[i] %= MOD

print(dp[N + 1])
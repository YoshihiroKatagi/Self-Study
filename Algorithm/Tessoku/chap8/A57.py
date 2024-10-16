N, Q = map(int, input().split())
A = list(map(int, input().split()))
queries = [ list(map(int, input().split())) for i in range(Q) ]

LEVELS = 30
dp = [ [ None ] * N for i in range(LEVELS)]

for i in range(0, N):
  dp[0][i] = A[i] - 1

for d in range(1, LEVELS):
  for i in range(0, N):
    dp[d][i] = dp[d-1][dp[d-1][i]]

for X, Y in queries:
  current_place = X - 1
  for d in range(29, -1, -1):
    if ((Y >> d) & 1) == 1:
    # if ( Y // (2 ** d)) % 2 == 1:
      current_place = dp[d][current_place]
  print(current_place + 1)
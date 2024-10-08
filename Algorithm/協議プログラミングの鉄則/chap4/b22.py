N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# dp = [ 10 ** 9 ] * (N + 1)
# dp[1] = 0
# dp[2] = A[0]

# for i in range(3, N+1):
#     dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# print(dp[N])

dp = [200000000] * N
dp[0] = 0

for i in range(N):
    if i <= N-2:
        dp[i+1] = min(dp[i+1], dp[i] + A[i])
    if i <= N-3:
        dp[i+2] = min(dp[i+2], dp[i] + B[i])

print(dp[N-1])
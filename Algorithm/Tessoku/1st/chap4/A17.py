N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [ None ] * (N+1)
dp[1] = 0
dp[2] = A[0]
for i in range(3, N+1):
  dp[i] = min(dp[i-1] + A[i-2], dp[i-2] + B[i-3])

ans = list()
x = N
while True:
  ans.append(x)
  if x == 1:
    break

  if dp[x] == dp[x-1] + A[x-2]:
    x -= 1
  else:
    x -= 2
  
ans.reverse()

Answer = [ str(i) for i in ans ]
print(len(Answer))
print(" ".join(Answer))
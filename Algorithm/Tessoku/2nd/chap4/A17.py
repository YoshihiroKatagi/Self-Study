N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [ None ] * (N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
  dp[i] = min(dp[i-1] + A[i-2], dp[i-2] + B[i-3])

answer = list()
Place = N
while True:
  answer.append(Place)
  
  if Place == 1:
    break

  if dp[Place] == dp[Place - 1] + A[Place - 2]:
    Place -= 1
  else:
    Place -= 2
  

answer.reverse()
print(len(answer))
print(*answer)
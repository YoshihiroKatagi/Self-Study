N = int(input())
h = list(map(int, input().split()))

dp = [None] * N

dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, N):
    dp[i] = min(dp[i-1] +  abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

Answer = []
Place = N-1
while True:
    Answer.append(Place+1)
    if Place == 0:
        break
    
    if dp[Place-1] + abs(h[Place] - h[Place-1]) == dp[Place]:
        Place = Place - 1
    else:
        Place = Place - 2
Answer.reverse()

Answer2 = [str(i) for i in Answer]
print(len(Answer))
print(" ".join(Answer2))
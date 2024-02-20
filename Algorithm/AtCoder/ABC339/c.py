N = int(input())
A = input().split()

ans = 0
for i in range(N):
  A_i = int(A[i])
  ans += A_i
  if ans < 0:
    ans = 0

print(ans)
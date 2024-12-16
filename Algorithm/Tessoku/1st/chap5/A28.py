N = int(input())
T = [ None ] * N
A = [ None ] * N
for i in range(N):
  T[i], A[i] = input().split()
  A[i] = int(A[i])

ans = 0
for i in range(N):
  if T[i] == "+":
    ans += A[i]
  if T[i] == "-":
    ans -= A[i]
  if T[i] == "*":
    ans *= A[i]
  
  if ans < 0:
    ans += 10000
  
  ans %= 10000
  print(ans)
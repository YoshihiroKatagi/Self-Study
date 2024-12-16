D = int(input())
N = int(input())
L = [ None ] * (N)
R = [ None ] * (N)
for i in range(N):
  L[i], R[i] = map(int, input().split())

A = [ 0 ] * (D+2)
for i in range(N):
  A[L[i]] += 1
  A[R[i]+1] -= 1

S = [ 0 ] * (D+1)
for i in range(1, D+1):
  S[i] = S[i-1] + A[i]
  print(S[i])


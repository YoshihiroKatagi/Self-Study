N = int(input())
A = list(map(int, input().split()))
D = int(input())
L = [ None ] * D
R = [ None ] * D
for i in range(D):
  L[i], R[i] = map(int, input().split())

P = [ None ] * N
P[0] = A[0]
for i in range(1, N):
  P[i] = max(P[i-1], A[i])

Q = [ None ] * N
Q[N-1] = A[N-1]
for i in reversed(range(0, N-1)):
  Q[i] = max(Q[i+1], A[i])

for d in range(D):
  print(max(P[(L[d]-1)-1], Q[(R[d]+1)-1]))

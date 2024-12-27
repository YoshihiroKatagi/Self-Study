import bisect

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

P = [ None ] * (N**2)
Q = [ None ] * (N**2)

for i in range(N):
  for j in range(N):
    P[i * N + j] = A[i] + B[j]

for i in range(N):
  for j in range(N):
    Q[i * N + j] = C[i] + D[j]

Q.sort()

for i in range(N*N):
  index = bisect.bisect_left(Q, K-P[i])
  if index < N*N and K-P[i] == Q[index]:
    print("Yes")
    exit()
print("No")
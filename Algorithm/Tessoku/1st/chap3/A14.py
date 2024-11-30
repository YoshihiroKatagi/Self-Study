import bisect
import sys

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

P = []
for x in range(N):
  for y in range(N):
    P.append(A[x] + B[y])

Q = []
for z in range(N):
  for w in range(N):
    Q.append(C[z] + D[w])

Q.sort()

for i in range(len(P)):
  pos1 = bisect.bisect_left(Q, K-P[i])
  if pos1<N*N and Q[pos1]==K-P[i]:
    print("Yes")
    sys.exit(0)

print("No")
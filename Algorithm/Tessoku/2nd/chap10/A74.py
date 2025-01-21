N = int(input())
P = [ list(map(int, input().split())) for i in range(N) ]

X = [ None ] * N
Y = [ None ] * N
for i in range(N):
  for j in range(N):
    if P[i][j] != 0:
      X[i] = P[i][j]
      Y[j] = P[i][j]

def inversion(A):
  answer = 0
  for i in range(N):
    for j in range(i + 1, N):
      if A[i] > A[j]:
        answer += 1
  return answer

print(inversion(X) + inversion(Y))
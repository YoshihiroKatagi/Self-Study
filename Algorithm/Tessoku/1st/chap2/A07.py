D = int(input())
N = int(input())
L = [ None ] * N
R = [ None ] * N
for i in range(N):
  L[i], R[i] = map(int, input().split())

B = [ 0 ] * (D+2)
for i in range(N):
  B[L[i]] += 1
  B[R[i] + 1] -= 1

ans = [ None ] * (D+2)
ans[0] = 0
for d in range(1,D+1):
  ans[d] = ans[d-1] + B[d]

for d in range(1, D+1):
  print(ans[d])
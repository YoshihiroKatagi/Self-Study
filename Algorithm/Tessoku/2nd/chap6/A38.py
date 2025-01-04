D, N = map(int, input().split())
L = [ None ] * N
R = [ None ] * N
H = [ None ] * N
for i in range(N):
  L[i], R[i], H[i] = map(int, input().split())

LIM = [24] * D
for i in range(N):
  for j in range(L[i]-1, R[i]):
    if LIM[j] > H[i]:
      LIM[j] = H[i]

ans = 0
for i in range(D):
  ans += LIM[i]

print(ans)
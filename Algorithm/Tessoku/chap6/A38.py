D, N = map(int, input().split())

L = [ None ] * N
R = [ None ] * N
H = [ None ] * N

for i in range(N):
  L[i], R[i], H[i] = map(int, input().split())

LIM = [ 24 ] * D
for i in range(N):
  l = L[i]
  r = R[i]
  for j in range(l-1, r):
    LIM[j] = min(LIM[j], H[i])

ans = sum(LIM)
print(ans)
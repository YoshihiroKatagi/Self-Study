N, L = map(int, input().split())
A = [ None ] * N
B = [ None ] * N
for i in range(N):
  A[i], B[i] = input().split()

ans = 0
for i in range(N):
  pos = int(A[i])
  direction = B[i]
  if direction == "E":
    ans = max(ans, L-pos)
  else:
    ans = max(ans, pos)

print(ans)

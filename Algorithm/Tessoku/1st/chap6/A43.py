N, L = map(int, input().split())
A = [ None ] * N
B = [ None ] * N
for i in range(N):
  a, b = input().split()
  A[i] = int(a)
  B[i] = b

ans = 0
for i in range(N):
  if B[i] == "E":
    dis = L - A[i]
  else:
    dis = A[i]
  
  ans = max(ans, dis)

print(ans)


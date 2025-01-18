N = int(input())

T = [ None ] * N
A = [ None ] * N

for i in range(N):
  T[i], A[i] = input().split()

ans = 0
for i in range(N):
  calc = T[i]
  a = int(A[i]) % 10000
  if calc == "+":
    ans = (ans + a) % 10000
  elif calc == "-":
    if ans - a < 0:
      ans = (ans - a + 10000) % 10000
    else:
      ans = (ans - a) % 10000
  else:
    ans = (ans * a) % 10000
  print(ans)
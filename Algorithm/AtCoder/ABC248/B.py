A, B, K = map(int, input().split())

def scream(a, k):
  return a*k

if A >= B:
  print(0)
  exit()

cnt = 0
while(A < B):
  A = scream(A, K)
  cnt+=1

print(cnt)
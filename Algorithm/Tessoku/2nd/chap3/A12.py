def check(M, A, N, K):
  sum = 0
  for i in range(N):
    sum += M // A[i]
    if sum >= K:
      return True
  return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = 10 ** 9
while L < R:
  M = (L + R) // 2
  ans = check(M, A, N, K)
  if ans == True:
    R = M
  else:
    L = M + 1

print(L)
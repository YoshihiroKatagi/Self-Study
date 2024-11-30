def check(x, N, K, A):
  sum = 0
  for i in range(N):
    sum += x // A[i]
  if sum >= K:
    return True
  else:
    return False

N, K = map(int, input().split())
A = list(map(int, input().split()))

Left = 1
Right = 10 ** 9
while Left < Right:
  Mid = (Left + Right) // 2
  ans = check(Mid, N, K, A)
  if ans == False:
    Left = Mid + 1
  else:
    Right = Mid
    
print(Left)
N, X = map(int, input().split())
A = list(map(int, input().split()))

L = 0
R = N
mid = (L+R) // 2

while True:
  if A[mid] == X:
    print(mid+1)
    break
  elif A[mid] < X:
    L = mid
  else:
    R = mid
  mid = (L+R)//2

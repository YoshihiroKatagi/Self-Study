N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
grundy = [ None ] * 100001

for i in range(100001):
  Transit = [False, False, False]
  if i >= X:
    Transit[grundy[i-X]] = True
  if i >= Y:
    Transit[grundy[i-Y]] = True
  if Transit[0] == False:
    grundy[i] = 0
  elif Transit[1] == False:
    grundy[i] = 1
  else:
    grundy[i] = 2

XOR_Sum = 0
for i in range(N):
  XOR_Sum = (XOR_Sum ^ grundy[A[i]])

if XOR_Sum >= 1:
  print("First")
else:
  print("Second")
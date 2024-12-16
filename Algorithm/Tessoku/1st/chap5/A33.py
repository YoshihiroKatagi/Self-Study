N = int(input())

A = list(map(int, input().split()))

XOR_Sum = A[0]
for i in range(1,N):
  XOR_Sum = (XOR_Sum ^ A[i])

if (XOR_Sum != 0):
  print("First")
else:
  print("Second")
N, K = map(int, input().split())

if K >= 2*(N-1) and K % 2 == 0:
  print("Yes")
else:
  print("No")
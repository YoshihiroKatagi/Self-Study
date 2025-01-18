X = int(input())
minus = 0
for i in range(1, 10):
  for j in range(1, i+1):
    if X == i*j:
      if i == j:
        minus += X
      else:
        minus += X * 2

Total = 2025
ans = Total - minus

print(ans)
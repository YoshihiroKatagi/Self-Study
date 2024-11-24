import math

N = int(input())
points = [list(map(float, input().split())) for i in range(N)]

ans = 0
x_1, y_1 = 0, 0

for i in range(N):
  x_2, y_2 = points[i]
  dis = math.sqrt((x_1 - x_2)**2 + (y_1 - y_2)**2)
  ans += dis
  x_1 = x_2
  y_1 = y_2

ans += math.sqrt(x_2**2 + y_2**2)

print(ans)



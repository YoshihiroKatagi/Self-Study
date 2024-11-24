import math

N, S, T = list(map(int, input().split()))

lines = [list(map(float, input().split())) for i in range(N)]

cur = [0.0, 0.0]
ans = 0.0

for a, b, c, d in lines:
  S_dis = math.sqrt((a - cur[0])**2 + (b - cur[1])**2)
  S_time = S_dis / S

  T_dis = math.sqrt((c - a)**2 + (d - b)**2)
  T_time = T_dis / T

  print("====")
  print(S_time)
  print(T_time)
  print("====")


  ans += (S_time + T_time)

  cur = [c, d]

print(ans)


# print(lines)

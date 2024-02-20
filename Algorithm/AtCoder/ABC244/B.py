import math

N = int(input())
T = list(input())

x = 0
y = 0
theta = math.pi/2
cnt=0

for i in range(N):
  if T[i]=="S":
    x += round(math.cos(theta*cnt))
    y += round(math.sin(theta*cnt))
  else:
    cnt-=1

print(x, y)
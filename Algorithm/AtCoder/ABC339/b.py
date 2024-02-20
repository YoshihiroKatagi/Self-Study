import math

H, W, N = input().split()
H = int(H)
W = int(W)
N = int(N)
field = [[0 for j in range(W)] for i in range(H)]
p = [0,0]
dir = math.pi

for i in range(N):
  if field[p[0]][p[1]] == 0:
    field[p[0]][p[1]] = 1
    dir -= math.pi / 2
  else:
    field[p[0]][p[1]] = 0
    dir +=math.pi / 2

  h = round(math.cos(dir))
  w = round(math.sin(dir))
  if p[0] == H-1 and h == 1:
    p[0] = 0
  elif p[0] == 0 and h == -1:
    p[0] = H-1
  elif p[1] == W-1 and w == 1:
    p[1] = 0
  elif p[1] == 0 and w == -1:
    p[1] = W-1
  else: 
    p[0] += h
    p[1] += w

for i in range(H):
  for j in range(W):
    if field[i][j] == 0:
      print(".", end="")
    else:
      print("#", end="")
  print()
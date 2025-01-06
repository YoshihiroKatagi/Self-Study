import math

def get_distance(x1, y1, x2, y2):
  return math.sqrt((x1-x2)**2 + (y1-y2)**2)

N = int(input())
X = [ None ] * N
Y = [ None ] * N
for i in range(N):
  X[i], Y[i] = map(int, input().split())

already = [ False ] * N

x1 = X[0]
y1 = Y[0]
print(1)
already[0] = True

while True:
  if False not in already:
    break

  distance = 10**9
  target_index = None
  for i in range(N):
    x_candi = X[i]
    y_candi = Y[i]
    dis_candi = get_distance(x1, y1, x_candi, y_candi)
    # print("dis_candi: " + str(dis_candi))
    if dis_candi < distance and already[i] == False:
      distance = dis_candi
      target_index = i

  print(target_index + 1)
  already[target_index] = True
  x1 = X[target_index]
  y1 = Y[target_index]

print(1)

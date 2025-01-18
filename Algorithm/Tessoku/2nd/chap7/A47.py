import random

class point2d:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def dist(self, p):
    return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** 0.5

def get_score(n, points, P):
  score = 0
  for i in range(n):
    score += points[P[i]].dist(points[P[i + 1]])
  return score

def hill_climbing(n, points):
  P = [ i % n for i in range(n + 1) ]
  current_score = get_score(n, points, P)
  NUM_LOOPS = 40000
  for t in range(NUM_LOOPS):
    l = random.randint(1, n - 1)
    r = random.randint(1, n - 1)
    if l > r:
      l, r = r, l
    P[l:r+1] = reversed(P[l:r+1])
    new_score = get_score(n, points, P)
    if current_score >= new_score:
      current_score = new_score
    else:
      P[l:r+1] = reversed(P[l:r+1])
  return P

N = int(input())
points = [ None ] * N
for i in range(N):
  x, y = map(int, input().split())
  points[i] = point2d(x, y)

answer = hill_climbing(N, points)

for i in answer:
  print(i + 1)
import numpy as np
import random
import time
import sys

N = 100
Q = 1000
A = np.array([ list(map(int, input().split())) for i in range(N) ])

X = [ random.randint(0, N - 1) for i in range(Q) ]
Y = [ random.randint(0, N - 1) for i in range(Q) ]
H = [ 1 ] * Q
B = np.zeros((3 * N, 3 * N))
for i in range(Q):
  B[Y[i]][X[i]] += 1

delta = [ None ] * (N + 1)
for i in range(1, N + 1):
  delta[i] = np.array([ [ max(i - abs(y) - abs(x), 0) for x in range(-i + 1, i) ] for y in range(-i + 1, i) ])

def get_score():
  return 200000000- np.absolute(A - B[N:2*N, N:2*N]).sum()

TIME_LIMIT = 5.4
current_score = get_score()
ti = time.time()

loops = 0
while time.time() - ti < TIME_LIMIT:
  t = random.randint(0, Q - 1)
  old_x, new_x = X[t], X[t] + random.randint(-9, +9)
  old_y, new_y = Y[t], T[t] + random.randint(-9, +9)
  old_h, new_h = H[t], H[t] + random.randint(-19, +19)
  if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or new_h <= 0 or new_h > N:
    continue
  
  B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] -= delta[H[t]]
  X[t], Y[t], H[t] = new_x, new_y, new_h
  B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] += delta[H[t]]

  new_score = get_score()

  if current_score < new_score:
    current_score = new_score
  else:
    B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] -= delta[H[t]]
    X[t], Y[t], H[t] = old_x, old_y, old_h
    B[N+Y[t]-H[t]+1:N+Y[t]+H[t], N+X[t]-H[t]+1:N+X[t]+H[t]] += delta[H[t]]
  
  loops += 1

print(Q)
for i in range(Q):
  print(X[i], Y[i], H[i])
print("score =", current_score, file = sys.stderr)
print("loops =", loops, file = sys.stderr)
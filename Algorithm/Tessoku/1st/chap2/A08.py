H, W = map(int, input().split())
X = [ None ] * H
for i in range(H):
  X[i] = list(map(int, input().split()))

Q = int(input())
query = [ None ] * Q
for i in range(Q):
  query[i] = list(map(int, input().split()))

Z = [ [ 0 ] * (W+1) for i in range(H+1) ]

for h in range(1, H+1):
  for w in range(1, W+1):
    Z[h][w] = Z[h][w-1] + X[h-1][w-1]

for w in range(1, W+1):
  for h in range(1, H+1):
    Z[h][w] = Z[h-1][w] + Z[h][w]

for i in range(Q):
  A, B, C, D = query[i]
  print(Z[C][D] + Z[A-1][B-1] - Z[A-1][D] - Z[C][B-1])
from collections import deque

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N + 1) ]

for a, b, c in edges:
  G[a].append([b, c])
  G[b].append([a, c])

# print(G)
Q = deque()
kakutei = [False] * (N + 1)
cur = [2000000000] * (N + 1)

cur[1] = 0
Q.append(cur[1], 1)

while Q.empty() == False:
  pos = Q.top()[1]
  Q.pop()

  if kakutei[pos] == True:
    continue

  kakutei[pos] = True
  for i in range(len(G[pos])):
    nex = G[pos][i][0]
    cost = G[pos][i][1]
    if cur[nex] > cur[pos] + cost:
      cur[nex] = cur[pos] + cost
      Q.append([cur[nex], nex])

for i in range(1, N):
  if cur[i] == 2000000000:
    print("-1")
  else:
    print(cur[i])

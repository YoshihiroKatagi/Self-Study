from collections import deque

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N + 1) ]

for a, b in edges:
  G[a].append(b)
  G[b].append(a)

dist = [ -1 ] * (N + 1)
dist[1] = 0
q = deque()
q.append(1)

while len(q) > 0:
  pos = q.popleft()
  for i in G[pos]:
    if dist[i] == -1:
      dist[i] = dist[pos] + 1
      q.append(i)

for i in range(1, N+1):
  print(dist[i])
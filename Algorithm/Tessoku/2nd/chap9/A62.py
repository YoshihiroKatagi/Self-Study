def dfs(pos, visited, G):
  visited[pos] = True
  for i in G[pos]:
    if not visited[i]:
      dfs(i, visited, G)

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

G = [ list() for i in range(N + 1) ]

for a, b in edges:
  G[a].append(b)
  G[b].append(a)

visited = [ False ] * (N + 1)
dfs(1, visited, G)

answer = "The graph is connected."
for i in range(1, N + 1):
  if not visited[i]:
    answer = "The graph is not connected."
    break

print(answer)
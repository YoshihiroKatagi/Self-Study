class maxflow_edge:
  def __init__(self, to, cap, rev):
    self.to = to
    self.cap = cap
    self.rev = rev
  
def dfs(pos, goal, F, G, used):
  if pos == goal:
    return F
  
  used[pos] =  True
  for e in G[pos]:
    if e.cap > 0 and not used[e.to]:
      flow = dfs(e.to, goal, min(F, e.cap), G, used)
      if flow >= 1:
        e.cap -= flow
        G[e.to][e.rev].cap += flow
        return flow
  return 0

def maxflow(N, s, t, edges):
  G = [ list() for i in range(N + 1) ]
  for a, b, c in edges:
    G[a].append(maxflow_edge(b, c, len(G[b])))
    G[b].append(maxflow_edge(a, 0, len(G[a]) - 1))
  
  INF = 10 ** 10
  total_flow = 0
  while True:
    used = [ False ] * (N + 1)
    F = dfs(s, t, INF, G, used)
    if F > 0:
      total_flow += F
    else:
      break
    
  return total_flow

N = int(input())
C = [ input() for i in range(N) ]

edges = []
for i in range(N):
  for j in range(N):
    if C[i][j] == '#':
      edges.append((i + 1, N + j + 1, 1))

for i in range(N):
  edges.append((2 * N + 1, i + 1, 1))
  edges.append((i + N + 1, 2 * N + 2, 1))

answer = maxflow(2 * N + 2, 2 * N + 1, 2 * N + 2, edges)
print(answer)
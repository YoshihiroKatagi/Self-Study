from collections import deque

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

graph = [ list() for i in range(N + 1) ]

for a, b in edges:
  graph[a].append(b)

def bfs_cycle(graph, start):
  visited = [-1] * (N+1)
  queue = deque([(start, 0)])
  # visited[start] = 0

  while queue:
    node, depth = queue.popleft()

    for neighbor in graph[node]:
      if neighbor == start:
        return depth + 1
      if visited[neighbor] == -1:
        visited[neighbor] = depth + 1
        queue.append((neighbor, depth + 1))
      # elif visited[neighbor] <= depth:
      #   return depth - visited[neighbor] + 1
  
  return -1

cycle_length = bfs_cycle(graph, 1)

print(cycle_length)
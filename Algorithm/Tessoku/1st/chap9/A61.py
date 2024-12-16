N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
  a, b = map(int, input().split())
  G[a-1].append(b)
  G[b-1].append(a)
  
for i in range(N):
  print(str(i + 1) + ": {", end="")
  for j in range(len(G[i])):
    if j >= 1:
      print(", ", end="")
    print(G[i][j], end="")
  print("}")


# N, M = map(int, input().split())
# edges = [ list(map(int, input().split())) for i in range(M) ]
# G = [ list() for i in range(N + 1) ]
# for a, b in edges:
#   G[a].append(b)
#   G[b].append(a)

# for i in range(1, N + 1):
#   output = ''
#   output += str(i)
#   output += ': {'
#   output += ', '.join(map(str, G[i]))
#   output += '}'
#   print(output)
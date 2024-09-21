N, M = map(int, input().split())
# A = list()
# B = list()
G = [[] for _ in range(N)]
for i in range(M):
  a, b = map(int, input().split())
  # A.append(a)
  # B.append(b)
  G[a-1].append(b)
  G[b-1].append(a)
  
# print(G)

for i in range(N):
  print(str(i + 1) + ": {", end="")
  for j in range(len(G[i])):
    if j >= 1:
      print(", ", end="")
    print(G[i][j], end="")

  print("}")
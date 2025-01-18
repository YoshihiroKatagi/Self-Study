class unionfind:
  def __init__(self, n):
    self.n = n
    self.par = [ -1 ] * (n + 1)
    self.size = [ 1 ] * (n + 1)

  def root(self, x):
    while self.par[x] != -1:
      x = self.par[x]
    return x
  
  def unite(self, u, v):
    rootu = self.root(u)
    rootv = self.root(v)
    if rootu == rootv:
      return
    if self.size[rootu] < self.size[rootv]:
      rootu, rootv = rootv, rootu
    self.par[rootv] = rootu
    self.size[rootu] += self.size[rootv]
  
  def same(self, u, v):
    return self.root(u) == self.root(v)

N, M = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(M) ]

edges.sort(key=lambda x: x[2])

uf = unionfind(N)
answer = 0
for a, b, c in edges:
  if not uf.same(a, b):
    uf.unite(a, b)
    answer += c

print(answer)
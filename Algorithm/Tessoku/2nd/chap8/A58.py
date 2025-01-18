class segtree:
  def __init__(self, n):
    self.size = 1
    while self.size < n:
      self.size *= 2
    self.dat = [0] * (self.size * 2)
  
  def update(self, pos, x):
    pos += self.size
    self.dat[pos] = x
    while pos > 0:
      pos //= 2
      self.dat[pos] = max(self.dat[pos * 2], self.dat[pos * 2 + 1])
  
  def query(self, l, r, a, b, u):
    if r <= a or b <= l:
      return -1000000000
    if l <= a and b <= r:
      return self.dat[u]
    m = (a + b) // 2
    answerl = self.query(l, r, a, m, u * 2)
    answerr = self.query(l, r, m, b, u * 2 + 1)
    return max(answerl, answerr)





N, Q = map(int, input().split())
queries = [ list(map(int, input().split())) for i in range(Q) ]

Z = segtree(N)
for q in queries:
  tp, *cont = q
  if tp == 1:
    pos, x = cont
    Z.update(pos - 1, x)
  if tp == 2:
    l, r = cont
    answer = Z.query(l - 1, r - 1, 0, Z.size, 1)
    print(answer)
def get_max(N, T, L, d):
  max_value = 0
  for i in range(N):
    weight = T[i] * (L[i] + d)
    max_value = max(max_value, weight)
  return max_value


N, D = map(int, input().split())

T = [ None ] * N
L = [ None ] * N

for i in range(N):
    T[i], L[i] = map(int, input().split())

for i in range(1, D+1):
  print(get_max(N, T, L, i))
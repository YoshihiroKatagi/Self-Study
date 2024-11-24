N = int(input())
q = [ None ] * (N+1)
r = [ None ] * (N+1)
for i in range(1, N+1):
  q[i], r[i] = map(int, input().split())

Q = int(input())
t = [ None ] * (Q+1)
d = [ None ] * (Q+1)
for i in range(1, Q+1):
  t[i], d[i] = map(int, input().split())

# print(q)
# print(r)
# print(t)
# print(d)

for i in range(1,Q+1):
  target_index = t[i]
  throw_date = d[i]
  q_i = q[target_index]
  r_i = r[target_index]
  # print(target_index, throw_date, q_i, r_i)
  # ans = (throw_date // q_i) + r_i - (throw_date % q[target_index])
  x = throw_date // q_i
  candi = q_i * x + r_i
  ans = 0
  if candi < throw_date:
    ans = candi + q_i
  else:
    ans = candi
  print(ans)


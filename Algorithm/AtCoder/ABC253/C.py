Q = int(input())
S = []
query = []
for i in range(Q):
  q = list(map(int, input().split()))
  query.append(q)
# print(query)

for i in range(Q):
  if query[i][0] == 1:
    S.append(query[i][1])

  elif query[i][0] == 2:
    x_num = S.count(query[i][1])
    x_remove = min(query[i][2], x_num)
    for j in range(x_remove):
      S.remove(query[i][1])
  
  else:
    S_max = max(S)
    S_min = min(S)
    dif = S_max - S_min
    print(dif)
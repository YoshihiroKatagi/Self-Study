N, Q = map(int, input().split())
queries = [ list(input().split()) for i in range(Q) ]

for i in range(Q):
  queries[i][1] = int(queries[i][1])

# print(queries)

ans = 0
pos_L = 1
pos_R = 2
for i in range(Q):
  h_i = queries[i][0]
  target = queries[i][1]

  if h_i == "R":
    if pos_R == target:
      continue
    if pos_L < pos_R:
      if pos_L < target and target < pos_R:
        ans += pos_R - target
      elif target > pos_R:
        ans += target - pos_R
      else:
        ans += N - pos_R + target
      pos_R = target
    else:
      if pos_R < target and target < pos_L:
        ans += target - pos_R
      elif target < pos_R:
        ans += pos_R - target
      else:
        ans += pos_R + N - target
      pos_R = target
  else:
    if pos_L == target:
      continue
    if pos_L < pos_R:
      if pos_L < target and target < pos_R:
        ans += target - pos_L
      elif target < pos_L:
        ans += pos_L - target
      else:
        ans += pos_L + N - target
      pos_L = target
    else:
      if pos_R < target and target < pos_L:
        ans += pos_L - target
      elif target > pos_L:
        ans += target - pos_L
      else:
        ans += N - pos_L + target
      pos_L = target

print(ans)
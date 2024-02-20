from collections import deque

Q = int(input())

Query = []
for i in range(Q):
  query = list(map(int, input().split()))
  Query.append(query)

ball = deque()

for q in Query:
  ans = 0
  if q[0] == 1:
    ball.append([q[1], q[2]])
  else:
    while(True):
      x, c = ball.popleft()
      if c > q[1]:
        ans += x * q[1]
        c -= q[1]
        ball.appendleft([x, c])
        break
      elif c == q[1]:
        ans += x * c
        break
      else:
        ans += x * c
        q[1] -= c

    print(ans)

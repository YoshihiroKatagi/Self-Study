from collections import deque

Q = int(input())

S = deque()

for i in range(Q):
  Query = input().split()

  if Query[0] == '1':
    S.append(Query[1])
  elif Query[0] == '2':
    print(S[0])
  else:
    S.popleft()
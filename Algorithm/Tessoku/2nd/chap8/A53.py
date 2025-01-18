import heapq

Q = int(input())

T = []

for i in range(Q):
  Query = input().split()

  if Query[0] == '1':
    heapq.heappush(T, int(Query[1]))
  elif Query[0] == '2':
    print(T[0])
  else:
    heapq.heappop(T)
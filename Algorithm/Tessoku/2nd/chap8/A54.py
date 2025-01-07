
Q = int(input())
queries = [ input().split() for i in range(Q) ]

Map = {}
for q in queries:
  if q[0] == '1':
    Map[q[1]] = q[2]
  else:
    print(Map[q[1]])

N, Q = map(int, input().split())
State = 1
E = [ None ] * (N+2)
for i in range(1, N+1):
  E[i] = i

for i in range(Q):
  Query = input().split()

  if int(Query[0]) == 1:
    x = int(Query[1])
    y = int(Query[2])
    if State == 1:
      E[x] = y
    if State == 2:
      E[N+1-x] = y
  
  if int(Query[0]) == 2:
    if State == 1:
      State = 2
    else:
      State = 1
  
  if int(Query[0]) == 3:
    x = int(Query[1])
    if State == 1:
      print(E[x])
    if State == 2:
      print(E[N+1-x])

# queries = [ list(map(int, input().split())) for i in range(Q) ]

# A = [ None ] * N
# for i in range(N):
#   A[i] = i+1

# state = 1
# for i in range(Q):
#   q = queries[i][0]

#   if q == 2:
#     if state == 1:
#       state = 2
#     else:
#       state = 1
#   else:
#     x = queries[i][1] - 1

#     if state == 2:
#       x = N - x - 1

#     if q == 1:
#         A[x] = queries[i][2]
#     else:
#       print(A[x])


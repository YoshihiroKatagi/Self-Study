N, Q = map(int, input().split())

A = [ None ] * (N+2)
for i in range(1, N+1):
  A[i] = i

flag = False

for i in range(Q):
  query = input().split()

  if query[0] == "1":
    x = int(query[1])
    y = int(query[2])
    if flag == False:
      A[x] = y
    else:
      A[N+1-x] = y
  
  elif query[0] == "2":
    if flag == False:
      flag = True
    else:
      flag = False

  else:
    x = int(query[1])
    if flag == False:
      print(A[x])
    else:
      print(A[N+1-x])

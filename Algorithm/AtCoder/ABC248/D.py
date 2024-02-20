N = int(input())
A = list(map(int, input().split()))
A = [0] + A
# print(A)
Q = int(input())
query = []
for i in range(Q):
  q = list(map(int, input().split()))
  query.append(q)
# print(query)

for q in query:
  cnt = 0
  # print(q)
  for i in range(q[0], q[1]+1):
    if A[i] == q[2]:
      cnt += 1
  print(cnt)
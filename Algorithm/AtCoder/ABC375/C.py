N = int(input())

A = [list(input()) for i in range(N)]

# print(A)
ans = [["."] * N for _ in range(N)]

for i in range(N):
  for j in range(N):
    d = min(i+1, j+1, N-1, N-j)
    ni = i
    nj = j
    for k in range(d%4):
      ti = nj
      tj = N - 1 - ni
      ni = ti
      nj = tj
    ans[ni][nj] = A[i][j]

for i in range(N):
  for j in range(N):
    print(ans[i][j], end="")
  print("")

# for i in range(N//2):
#   for x in range(N):
#     for y in range(N):
#       if x < i or x >= N-i or y < i or y >= N-i:
#         continue
#       B[y][N-1-x] = A[x][y]
    


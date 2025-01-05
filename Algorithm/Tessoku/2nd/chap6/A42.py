N, K = map(int, input().split())
A = [ None ] * N
B = [ None ] * N
for i in range(N):
  A[i], B[i] = map(int, input().split())

count = [ 0 ] * N
for A_min in range(1, 101-K):
  for B_min in range(1, 101-K):
    A_max = A_min + K
    B_max = B_min + K
    cnt = 0
    for i in range(N):
      if A_min <= A[i] <= A_max and B_min <= B[i] <= B_max:
        cnt += 1
    count[i] = max(count[i], cnt)

ans = max(count)
print(ans)
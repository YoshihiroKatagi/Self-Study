N, M = map(int, input().split())

X = list(map(int, input().split()))
A = list(map(int, input().split()))

sorted_pairs = sorted(zip(X, A))

X_sorted, A_sorted = zip(*sorted_pairs)
X = list(X_sorted)
A = list(A_sorted)

if sum(A) != N:
  print(-1)
  exit()

if X[0] != 1:
  print(-1)
  exit()

ans = 0
for i in range(M):
  if i == M-1:
    next_box = N+1
  else:
    next_box = X[i+1]
  current_box = X[i]
  box_diff = next_box - current_box
  
  if A[i] < box_diff:
    print(-1)
    exit()
  
  leftover = A[i] - box_diff
  if i != M-1:
    A[i+1] += leftover
  
  ans += (box_diff-1)*box_diff//2 + leftover * box_diff

print(ans)
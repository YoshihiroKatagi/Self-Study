from bisect import bisect_right

def get_count_less_than_x(A, x):
  count = bisect_right(A, x)
  if count >= 0:
    return count
  else:
    return -1

N = int(input())
A = list(map(int, input().split()))

answer = 0
for i in range(N):
  x = A[i] // 2
  count = get_count_less_than_x(A, x)
  if count >= 0:
    answer += count

print(answer) 
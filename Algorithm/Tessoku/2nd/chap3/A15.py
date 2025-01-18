import bisect

N = int(input())
A = list(map(int, input().split()))

T = sorted(set(A))
B = [ None ] * N
for i in range(N):
  B[i] = bisect.bisect_left(T, A[i]) + 1

print(*B)


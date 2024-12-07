import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

filtered_A = []
current_min = 10000000

for i in range(N):
  if A[i] < current_min:
    filtered_A.append((A[i], i))
    current_min = A[i]

filtered_A.sort()

filtered_values = [x[0] for x in filtered_A]
filtered_indices = [x[1] for x in filtered_A]


for b in B:
  pos = bisect.bisect_right(filtered_values, b) - 1
  if pos >=0 and filtered_values[pos] <= b:
    print(filtered_indices[pos] + 1)
  else:
    print(-1)



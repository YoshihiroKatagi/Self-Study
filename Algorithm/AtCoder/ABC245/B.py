N = int(input())
A = list(map(int, input().split()))

integer = []
for i in range(3000):
  integer.append(i)

for i in range(N):
  if A[i] in integer:
    integer.remove(A[i])

print(min(integer))
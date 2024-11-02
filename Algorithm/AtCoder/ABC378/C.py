N = int(input())
A = list(map(int, input().split()))

Already = {} 
B = list()

for i in range(N):
  if A[i] not in Already:
    B.append(-1)
  else:
    B.append(Already[A[i]])

  Already[A[i]] = i+1

print(*B)
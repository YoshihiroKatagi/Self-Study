N = int(input())
A = []
for i in range(N):
  l, r = map(int, input().split())
  A.append([r, l])

A.sort()

CurrentTime = 0
Answer = 0
for i in range(N):
  if CurrentTime <= A[i][1]:
    CurrentTime = A[i][0]
    Answer += 1

print(Answer)
N, C = input().split()
N = int(N)
A = input()

score = 0
for i in range(N):
  a = A[i]
  if a == "B":
    score += 1
  elif a == "R":
    score += 2

if C == "W" and score % 3 == 0:
  print("Yes")
elif C == "B" and score % 3 == 1:
  print("Yes")
elif C == "R" and score % 3 == 2:
  print("Yes")
else:
  print("No")
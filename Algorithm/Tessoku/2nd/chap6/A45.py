N, C = input().split()
A = input()

N = int(N)
total_score = 0
for i in range(N):
  if A[i] == "B":
    total_score += 1
  elif A[i] == "R":
    total_score += 2

final_score = total_score % 3
if (final_score == 0 and C == "W") or (final_score == 1 and C == "B") or (final_score == 2 and C == "R"):
  print("Yes")
else:
  print("No")
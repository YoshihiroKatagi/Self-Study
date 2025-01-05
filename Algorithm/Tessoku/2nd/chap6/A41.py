N = int(input())
S = input()

ans = False
for i in range(N-2):
  S_1 = S[i]
  S_2 = S[i+1]
  S_3 = S[i+2]
  if S_1 == "R" and S_2 == "R" and S_3 == "R":
    ans = True
  if S_1 == "B" and S_2 == "B" and S_3 == "B":
    ans = True

if ans:
  print("Yes")
else:
  print("No")

S = input()
T = input()

ans = 0

if len(S) == len(T):
  for i in range(len(S)):
    S_i = S[i]
    T_i = T[i]
    if S_i != T_i:
      ans = i + 1
      break
elif len(S) < len(T):
  for i in range(len(S)):
    S_i = S[i]
    T_i = T[i]
    if S_i != T_i:
      ans = i + 1
      break
  if ans == 0:
    ans = len(S) + 1
else:
  for i in range(len(T)):
    S_i = S[i]
    T_i = T[i]
    if S_i != T_i:
      ans = i + 1
      break
  if ans == 0:
    ans = len(T) + 1

print(ans)

N = int(input())
S = input()
T = input()

if (T[0] == "B" and S[0] != T[0]):
  print("-1")
elif (T[-1] == "A" and S[-1] != T[-1]):
  print("-1")
else:
  ans = 0
  count_BtoA = 0
  count_AtoB = 0
  flag = 0

  for i in range(N):
    if (i == 0):
      count_BtoA += 1
      continue
    if flag == 0:
      if (S[i] == "B" and T[i] == "A"):
        count_BtoA += 1
      elif (S[i] == T[i]):
        continue
      elif (S[i] == "A" and T[i] == "B" and i != N-1):
        count_AtoB += 1
        flag = 1
        continue
      else:
        ans += count_BtoA
        continue
    elif flag == 1:
      if (S[i] == T[i]):
        if (i == N-1):
          ans += count_BtoA
      elif (S[i] == "A" and T[i] == "B"):
        count_AtoB += 1
        if (i == N - 1):
          ans += max(count_AtoB, count_BtoA)
      else:
        ans += max(count_AtoB, count_BtoA)
        count_AtoB = 0
        count_BtoA = 1
        flag = 0

print(ans)
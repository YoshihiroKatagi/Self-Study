N = int(input())
A = input().split()
print(A)

ans = []

def check(P_i):
  tmp = []
  A_i = int(A[P_i])
  if A_i not in ans:
    if A_i == -1:
      ans.append(P_i + 1)
      for p in reversed(tmp):
        ans.append(p + 1)
      return
    else:
      tmp.append(P_i)
      return check(A_i - 1)
  else:
    ans.append(P_i + 1)
    return

for i in range(N):
  if i+1 not in ans:
    check(i)
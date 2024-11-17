S = input()

ans = list()
count = 0
for i in range(len(S)):
  if S[i] == "-":
    count += 1

  if i != 0 and S[i] == "|":
    ans.append(count)
    count = 0
    

print(*ans)


H, W = map(int, input().split())
S = []
for i in range(H):
  s = input()
  S.append(s)
# print(S)

P = []
for i in range(H):
  for j in range(W):
    if S[i][j] == "o":
      p = [i, j]
      P.append(p)
# print(P)

dif_h = abs(P[0][0] - P[1][0])
dif_w = abs(P[0][1] - P[1][1])

ans = dif_h + dif_w
print(ans)
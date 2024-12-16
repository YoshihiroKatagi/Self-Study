N, D = map(int, input().split())
S = input()

k_count = 0
for i in range(N):
  if S[i] == "@":
    k_count += 1

ans = N - (k_count - D)
print(ans)
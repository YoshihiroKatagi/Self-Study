N, D = map(int, input().split())
S = input()

k_count = 0
for i in range(N):
  if S[i] == "@":
    k_count += 1

left_count = k_count - D

count = 0
ans = ""
for i in range(N):
  if S[i] == "@" and count < left_count:
    ans += "@"
    count += 1
  else:
    ans += "."

print(ans)
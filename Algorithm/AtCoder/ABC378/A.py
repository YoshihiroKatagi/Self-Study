A1, A2, A3, A4 = map(int, input().split())
count = [0] * 5
for i in range(1, 5):
  if A1 == i:
    count[i] += 1
  if A2 == i:
    count[i] += 1
  if A3 == i:
    count[i] += 1
  if A4 == i:
    count[i] += 1

ans = 0
for i in range(1,5):
  if count[i] > 1:
    ans += count[i] // 2

print(ans)
N = int(input())
A = list(map(int, input().split()))

count = [ 0 ] * 101
for i in range(N):
  count[A[i]] += 1

ans = 0
for i in range(1, 101):
  ans += count[i] * (count[i] - 1) * (count[i] - 2) // 6

print(ans)
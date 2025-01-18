N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for a in A:
  ans += a * M

for c in C:
  ans += c * N

ans += B * (N*M)

print(ans)
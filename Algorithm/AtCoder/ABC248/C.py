mod = 998244353
ans = 0

N, M, K = map(int, input().split())
A = [1 for i in range(N)]
# print(A)

middle_num = K // N
print(middle_num)
ans += N**middle_num
print(ans)

amari = K - middle_num * N
print(amari)

for i in range(amari):
  


ans %= mod
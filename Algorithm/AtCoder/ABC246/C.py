N, K, X = map(int, input().split())
A = list(map(int, input().split()))

price = 0
for a in A:
  price += a

amari = [0] * N
for i in range(N):
  coupon = A[i] // X
  amari[i] = A[i] % X
  if K>=coupon:
    price -= coupon * X
    K -= coupon
  else:
    price -= K * X
    K -= K
  if K==0:
    break

print(price)
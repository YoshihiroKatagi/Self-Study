M = int(input())

ANS = [0] * (M+1)

A = list()

a_max = 10
calc = M

while calc > 0:
  pow_3 = 3**a_max
  if pow_3 <= calc:
    calc -= pow_3
    A.append(a_max)
  else:
    a_max -= 1

print(len(A))
print(" ".join(map(str, A)))
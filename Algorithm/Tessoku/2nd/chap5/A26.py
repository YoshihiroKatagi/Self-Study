def check(x):
  limit = int(x ** 0.5)
  for i in range(2, limit+1):
    if x % i == 0:
      return True


Q = int(input())

for i in range(Q):
  X = int(input())
  ans = check(X)
  if ans == True:
    print("No")
  else:
    print("Yes")
S = str(input())
num = [int(a) for a in str(S)]

for i in range(10):
  if not i in num:
    print(i)
    exit()



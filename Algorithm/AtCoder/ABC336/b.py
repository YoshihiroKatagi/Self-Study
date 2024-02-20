N = int(input())
b = ''
while(N>0):
  bit = str(N % 2)
  b = bit + b
  N = N // 2

# print(b)
ans = 0
b = int(b)
while(True):
  check = b % 10
  if check == 0:
    ans += 1
    b = b // 10
  else:
    break
print(ans)

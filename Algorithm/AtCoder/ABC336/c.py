N = int(input())
b = ''
while(N>0):
  bit = str(N % 5)
  b = bit + b
  N = N // 5
b = str(int(b) - 1)
# print(b)
ans = ''
for i in range(len(b)):
  s = int(b[i])
  ans = ans + str(s * 2)
print(ans)

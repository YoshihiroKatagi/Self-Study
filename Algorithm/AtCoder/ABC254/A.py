N = int(input())

ans = N % 100

if ans < 10:
  ans = "0" + str(ans)

print(ans)
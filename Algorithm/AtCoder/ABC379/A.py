N = int(input())
a = str(N // 100)
b = str((N % 100) // 10)
c = str(N % 10)

ans1 = b + c + a
ans2 = c + a + b
print(ans1, ans2)
N = int(input())
A = list(input().split())

ans = 0

for i in range(N):
    for j in range(i+1, N):
        string_number = A[i] + A[j]
        ans += int(string_number)
print(ans%998244353)

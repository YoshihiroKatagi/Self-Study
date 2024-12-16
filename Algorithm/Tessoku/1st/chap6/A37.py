N, M, B = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
Sum_A = sum(A)
Sum_C = sum(C)
ans = Sum_A * M + B * (N*M) + Sum_C * N

print(ans)
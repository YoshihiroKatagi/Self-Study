N, K = map(int, input().split())
A = list(map(int,input().split()))

ans = list()
for i in range(N):
    # print(A[i] % K)
    # print(A[i] // K)
    if A[i] % K == 0:
        # ans.append(A[i] // K)
        print(A[i] // K, end = ' ')

# print()
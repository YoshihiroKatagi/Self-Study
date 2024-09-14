N, L, R = map(int, input().split())

A = list(range(1, N+1))

L -= 1
R -= 1

A[L:R+1] = A[L:R+1][::-1]

for i in range(N):
    print(A[i], end=' ')


# ans = list()
# for i in range(N):
#     if i >= L-1 and i <= R-1:
#         ans.append(N - i)
#     else:
#         ans.append(i+1)

# for i in range(N):
#     print(ans[i], end=' ')
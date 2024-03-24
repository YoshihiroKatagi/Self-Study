N, K = map(int,input().split())
A = list(map(int, input().split()))

S_K = K * (1 + K) // 2

new_list = set()

for i in range(len(A)):
    if A[i] <= K:
        new_list.add(A[i])

A_total = sum(new_list)

# print(S_K)
# print(A_total)

ans = S_K - A_total
print(ans)


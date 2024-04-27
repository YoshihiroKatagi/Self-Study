N, Q = map(int, input().split())
T = list(map(int, input().split()))

ans = [1] * N
# print(ans)

for i in range(len(T)):
    if ans[T[i]-1] == 1:
        ans[T[i]-1] = 0
    else:
        ans[T[i]-1] = 1

# print(ans)
ans_count = ans.count(1)

print(ans_count)
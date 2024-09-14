N, K = map(int, input().split())
A = list(map(int, input().split()))

ans = 1
seat = K

for i in range(N):
    # print("----")
    # print("i:" + str(i))
    # print("ans:" + str(ans))
    # print("seat:" + str(seat))
    # print("----")

    if A[i] <= seat:
        seat-=A[i]
    else:
        ans+=1
        seat=K-A[i]

print(ans)
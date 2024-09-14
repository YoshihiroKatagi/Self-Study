N = int(input())
A = list(map(int, input().split()))

ball_list = list()

for i in range(N):
    # print(i)
    ball_list.append(A[i])
    # print(ball_list)
    while(len(ball_list) > 1):
        if ball_list[-1] != ball_list[-2]:
            break
        else:
            # print(ball_list[-1])
            # print(ball_list[-2])
            size_sum = ball_list[-1] + 1
            ball_list = ball_list[:-2]
            ball_list.append(size_sum)
            # print(ball_list)

# count = 0
# r = list()
# for i in range(N):
#     if len(r) == 0:
#         r.append(A[i])
#     if len(r) > 0 and r[-1] == A[i]:
#         r = list()
#         r.append(r[0]+1)
#     elif len(r) > 0 and r[-1] == A[i] + 1:
#         r.append(A[i])
#     else:
#         count+=len(r)
#         r = list()
# print(count + len(r))


count = 0
ans = list()
r = list()
for i in range(N):
    r.append(A[i])
    if (len(r) > 1):
        if r[-2] > r[-1]:
            ans.append(r[-2])
        elif r[-2] == r[-1]:
            r = r[:-2]
            r.append(A[i] + 1)
        else:
            





    if len(r) == 0:
        r.append(A[i])
    if len(r) > 0 and r[-1] == A[i]:
        r = list()
        r.append(r[0]+1)
    elif len(r) > 0 and r[-1] == A[i] + 1:
        r.append(A[i])
    else:
        count+=len(r)
        r = list()
print(count + len(r))



# print(len(ball_list))
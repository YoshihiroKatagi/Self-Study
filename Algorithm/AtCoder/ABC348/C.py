N = int(input())

Beans = list()
A_list = list()
C_list = list()

for i in range(N):
    bean = list(map(int, input().split()))
    Beans.append(bean)

# print(Beans)

for i in range(N):
    a = Beans[i][0]
    c = Beans[i][1]
    # print("a, c : " + str(a) + ", " + str(c))
    if c not in C_list:
        # print("not in C_List")
        A_list.append(a)
        C_list.append(c)
    else:
        # print("compare with A_list")
        index = C_list.index(c)
        if a < A_list[index]:
            A_list[index] = a

ans = max(A_list)

# print(A_list)
# print(C_list)

print(ans)
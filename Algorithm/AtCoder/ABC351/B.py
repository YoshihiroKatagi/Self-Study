N = int(input())

A = list()
B = list()

for i in range(N):
    a_i = input()
    A.append(a_i)

for i in range(N):
    b_i = input()
    B.append(b_i)

# print(A)
# print(B)

for i in range(N):
    for j in range(N):
        # print("===")
        # print(str(i) + " " + str(j))
        # print(A[i][j])
        # print(B[i][j])
        # print("===")
        if A[i][j] != B[i][j]:
            print(str(i+1) + " " + str(j+1))
            break


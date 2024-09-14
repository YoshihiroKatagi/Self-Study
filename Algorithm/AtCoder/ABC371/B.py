N, M = map(int, input().split())
A = list()
B = list()
Flag = [0] * N
for i in range(M):
  a, b = map(str, input().split())
  A.append(int(a))
  B.append(b)

for i in range(M):
  A_i = A[i]
  B_i = B[i]
  flag_i = Flag[A_i-1]
  # print("=====")
  # print(A_i)
  # print(B_i)
  # print(flag_i)
  # print("=====\n")
  if B_i == 'M' and flag_i == 0:
    print("Yes")
    Flag[A_i-1] = 1
  else:
    print("No")
# print(Flag)

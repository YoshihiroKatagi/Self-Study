N = int(input())
A = list(map(int, input().split()))

new_list = list()
count = 0
ans = ""

for i in range(N-1):
    if A[0] == i+1:
        A.pop(0)

    else:
        min_index = A.index(i+1)
        ans += str(i+1) + " " + str(min_index+i+1) + "\n"
        A[min_index] = A[0]
        A.pop(0)
        count+=1

# for i in range(N-1):
#     if A[i] == i+1:

#         continue
#     else:
#         # print("i: " + str(i))
#         min_index = A.index(i+1)
#         # min_index = A[i+1:].index(i+1) + i + 1
#         ans += str(i+1) + " " + str(min_index+1) + "\n"
#         A[min_index] = A[i]
#         A[i] = i+1
#         count += 1


print(count)
print(ans)

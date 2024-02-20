N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
like_list = []
favorite = max(A)
for i in range(len(A)):
  if A[i] == favorite:
    like_list.append(i+1)

for i in like_list:
  if i in B:
    print('Yes')
    exit()

print('No')
  
  
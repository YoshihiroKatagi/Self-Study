N, A, B = map(int, input().split())
D = list(map(int, input().split()))

C = A + B - 1
clist = [True] * C

for i in range(N):
    D_i = D[i]
    n=D_i // (A+B)
    for i1 in range(D_i - (A+B)*n + 1, A + B - 1):
        clist[i1] =False
    for i1 in range(D_i - (A+B)*n - A):
        clist[i1] =False

f = False
for i in range(A + B - 1):
    if clist[i] == True:
        f = True
        break

if f == True:
    print('Yes')
else:
    print('No')
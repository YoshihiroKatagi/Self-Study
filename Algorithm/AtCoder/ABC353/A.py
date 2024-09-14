N = int(input())
H = list(map(int, input().split()))

flag = False

for i in range(len(H)):
    if i == 0:
        continue
    
    if H[i] > H[0]:
        print(i+1)
        flag = True
        break
if flag == False:
    print(-1)
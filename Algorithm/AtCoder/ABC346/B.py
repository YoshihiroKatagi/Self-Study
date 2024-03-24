S = "wbwbwwbwbwbw"
S_inf = S + S + S + S + S + S + S + S + S + S + S + S + S + S + S + S + S + S + S + S

itr_count = 12
flag = 0

W, B = map(int,input().split())

for initial in range(itr_count):
    w_cnt = 0
    b_cnt = 0
    for i in range(W+B):
        if (S_inf[initial + i] == "w"):
            w_cnt+=1
        else:
            b_cnt+=1
    if w_cnt == W and b_cnt == B:
        flag = 1
        print("Yes")
        break

if flag == 0:
    print("No")





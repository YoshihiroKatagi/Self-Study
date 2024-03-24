S = input()
flag = 1
if S[0] != "<":
    flag = 0
if S[-1] != ">":
    flag = 0
for i in range(len(S)-2):
    if S[i+1] != "=":
        flag = 0
        break

if flag == 1:
    print("Yes")
else:
    print("No")
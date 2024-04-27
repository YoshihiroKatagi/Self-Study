S = input()

contest_num = ""
for i in range(len(S)):
    if i < 3:
        continue
    contest_num += S[i]

ans = int(contest_num)

if (ans == 316):
    print("No")
elif (ans > 0 and ans < 350):
    print("Yes")
else:
    print("No")
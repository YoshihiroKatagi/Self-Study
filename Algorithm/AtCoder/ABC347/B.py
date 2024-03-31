S = input()

ans_list = list()

S_len = len(S)

for i in range(S_len):
    for j in range(1, S_len+1):
        if i + j > S_len:
            continue
        target = S[i:i + j]
        if target not in ans_list:
            ans_list.append(target)

# print(ans_list)
print(len(ans_list))
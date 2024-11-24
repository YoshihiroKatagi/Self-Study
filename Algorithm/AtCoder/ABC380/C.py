N, K = map(int, input().split())
S = input()

ans_list = ["0"] * N

count = 0
change_index = 0
count_flag = False
change_list = list()

for i in range(N):
  if count_flag == False:
    if S[i] == "1":
      count_flag = True
      count += 1
      if count == K:
        change_list.append(change_index)
        change_index += 1
      else:
        change_list.append(i)
    
  else:
    if S[i] == "1":
      if count == K:
        change_list.append(change_index)
        change_index += 1
      else:
        change_list.append(i)
    else:
      count_flag = False
      if count == K-1:
        change_index = i

for index in change_list:
  ans_list[index] = "1"

ans = "".join(ans_list)
print(ans)

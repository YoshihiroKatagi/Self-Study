S = input()

ans_count = 0
zero_flag = False
for i in range(len(S)):
  if S[i] != "0":
    ans_count += 1
  else:
    if zero_flag == False:
      if i == len(S)-1:
        ans_count += 1
        break
      if S[i+1] == "0":
        ans_count += 1
        zero_flag = True
      else:
        ans_count += 1
    else:
      zero_flag = False

print(ans_count)
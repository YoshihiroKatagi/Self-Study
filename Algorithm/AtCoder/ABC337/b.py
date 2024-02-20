s = input()
s_1 = s[0]
check = ["A", "B", "C"]
check_num = 0
flag = 0
for i in range(len(s)):

  if check[check_num] == "C":
    if s[i] == check[check_num]:
      continue
    else:
      print("No")
      flag = 1
      break
  else:
    if s[i] == check[check_num]:
      continue
    elif s[i] == check[check_num + 1]:
      check_num+=1
      continue
    elif  check[check_num]=="A" and s[i] == check[check_num + 2]:
      check_num+=2
      continue
    else:
      flag = 1
      print("No")
      break
if flag == 0:
  print("Yes")
N = input()

count_1 = 0
count_2 = 0
count_3 = 0

for i in range(len(N)):
  if N[i] == "1":
    count_1 += 1
  if N[i] == "2":
    count_2 += 1
  if N[i] == "3":
    count_3 += 1
  
if count_1 == 1 and count_2 == 2 and count_3 == 3:
  print("Yes")
else:
  print("No")
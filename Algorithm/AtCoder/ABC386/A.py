Cards = list(map(int, input().split()))

kind1 = None
kind2 = None
count1 = 0
count2 = 0

for i in range(len(Cards)):
  if i == 0:
    kind1 = Cards[i]
    count1 += 1
  else:
    if Cards[i] == kind1:
      count1 += 1
    else:
      if kind2 == None:
        kind2 = Cards[i]
      if Cards[i] == kind2:
        count2 += 1
      
# print(count1, count2)
if (count1 == 2 and count2 == 2) or (count1 == 3 and count2 == 1) or (count1 == 1 and count2 == 3):
  print("Yes")
else:
  print("No")
      
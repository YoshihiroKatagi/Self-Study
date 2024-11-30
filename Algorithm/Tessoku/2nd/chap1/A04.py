N = int(input())

for x in [9,8,7,6,5,4,3,2,1,0]:
  wari = (2 ** x)
  print((N // wari) % 2, end="")
S_1, S_2, S_3 = map(str, input().split())
T_1, T_2, T_3 = map(str, input().split())

if S_1==T_1 and S_2==T_2 and S_3==T_3:
  print("Yes")
elif S_1!=T_1 and S_2!=T_2 and S_3!=T_3:
  print("Yes")
else:
  print("No")
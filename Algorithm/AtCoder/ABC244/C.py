N = int(input())

rest_num = []
for i in range(1, 2*N+2):
  rest_num.append(i)

while rest_num:
  declare_num = rest_num[0]
  print(declare_num)
  rest_num.remove(declare_num)
  if rest_num:
    aoki_num = int(input())
    rest_num.remove(aoki_num)
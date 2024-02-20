a, b, c = map(int, input().split())

l = [a, b, c]
l.sort()
# print(l)

if b == l[1]:
  print("Yes")
else:
  print("No")
X = int(input())
li = []
ans = 1
li.append(X)
while len(li) > 0:
  tmp = li.pop(0)
  if tmp % 2 == 0:
    if tmp <= 4:
      ans *= tmp
    else:
      li.append(int(tmp/2))
      li.append(int(tmp/2))
  else:
    if tmp < 5:
      ans *= tmp
    else:
      li.append(int((tmp-1)/2))
      li.append(int((tmp+1)/2))
print (int(ans % 998244353))
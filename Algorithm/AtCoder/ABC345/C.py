from collections import OrderedDict

S = input()

flag = 0

S_formed = ''.join(OrderedDict.fromkeys(S))
length = len(S_formed)
ans = length * (length - 1) // 2

if (S != S_formed):
    ans += 1

print(ans)
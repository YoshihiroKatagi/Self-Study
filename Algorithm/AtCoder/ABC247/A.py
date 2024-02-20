S = str(input())

new_S = []
new_S.append('0')

for i in range(3):
  if (S[i] == '1'):
    new_S.append('1')
  else:
    new_S.append('0')

ans = ''.join(new_S)

print(ans)
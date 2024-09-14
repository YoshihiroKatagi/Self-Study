ab, ac, bc = map(str, input().split())

ans = ''

if ab == '<':
  if bc == '<':
    ans = 'B'
  else:
    if ac == '<':
      ans = 'C'
    else:
      ans = 'A'
else:
  if ac == '<':
    ans = 'A'
  else:
    if bc == '<':
      ans = 'C'
    else:
      ans = 'B'

print(ans)
N = int(input())

def S_n(n):
  if n == 1:
    return 1
  else:
    s_pre = S_n(n-1)
    if s_pre == 1:
      new_S = ['1', '2', '1']
    else:
      new_S = s_pre + [str(n)] + s_pre
    return new_S

if N == 1:
  print(1)
  exit()
print(' '.join(S_n(N)))
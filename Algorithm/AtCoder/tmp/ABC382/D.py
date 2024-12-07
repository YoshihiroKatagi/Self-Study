N, M = map(int, input().split())

first_count = M % 10

for i in range(1, N+1):
  new_list = list()
  while len(new_list) < N:
    new_list.append(i)
    

N = int(input())
name = []
for i in range(N):
  s, t = map(str, input().split())
  name.append([s, t])

for i in range(N):
  last_count = 0
  first_count = 0
  for j in range(N):
    s, t = name[i]
    if s in name[j]:
      last_count+=1
    if t in name[j]:
      first_count+=1
  if last_count>=2 and first_count>=2:
    print("No")
    exit()

print("Yes")
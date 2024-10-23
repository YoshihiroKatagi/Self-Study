N = int(input())
# A = []
# for i in range(N):
#   l, r = map(int, input().split())
#   A.append([r, l])
L = [ None ] * N
R = [ None ] * N
movies = [ list(map(int, input().split())) for i in range(N) ]

# A.sort()

movies_sorted = sorted(movies, key=lambda x: x[1])

current_time = 0
ans = 0
for i in range(N):
  start_time = movies_sorted[i][0]
  end_time = movies_sorted[i][1]
  if current_time <= start_time:
    ans += 1
    current_time = end_time

# print(movies_sorted)
print(ans)
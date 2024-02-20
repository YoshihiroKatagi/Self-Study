# N = int(input())

# people = []

# for i in range(N):
#   X, Y = map(int, input().split())
#   people.append([X, Y])

# S = list(input())

# for i in range(N):
#   for j in range(N):
#     if people[i][1]==people[j][1]:
#       if people[i][0]<people[j][0] and S[i]=='R' and S[j]=='L':
#         print('Yes')
#         exit()
#       elif people[i][0]>people[j][0] and S[i]=='L' and S[j]=='R':
#         print('Yes')
#         exit()

# print('No')



#sample answer
N = int(input())
X, Y = [], []
for _ in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)
S = input()
right_min, left_max = dict(), dict()
for i in range(N):
  if S[i] == 'R':
    if Y[i] in left_max and X[i] < left_max[Y[i]]:
      Yes()
  else:
    if Y[i] in right_min and right_min[Y[i]] < X[i]:
      Yes()
  if S[i] == 'R':
    if Y[i] in right_min:
      right_min[Y[i]] = min(X[i], right_min[Y[i]])
    else:
      right_min[Y[i]] = X[i]
  else:
    if Y[i] in left_max:
      left_max[Y[i]] = max(X[i], left_max[Y[i]])
    else:
      left_max[Y[i]] = X[i]
print("No")
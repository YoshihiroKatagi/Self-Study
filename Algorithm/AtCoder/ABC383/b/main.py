## 2 values
# N, M = map(int, input().split())

## 2 lists
## input:
## A_i B_i
## 1   2
## 3   4
## 5   6
# A = [ None ] * N
# B = [ None ] * N
# for i in range(N):
#   A[i], B[i] = map(int, input().split())

# A = list(map(int, input().split()))
# B = list(map(int, input().split()))

H, W, D = map(int, input().split())

S = [ None ] * H

for i in range(H):
  S[i] = input()


ans = 0
for h1 in range(H):
  for w1 in range(W):
    for h2 in range(H):
      for w2 in range(W):
        already = [[False for _ in range(W)] for _ in range(H)]
        count = 0
        for i in range(H):
          for j in range(W):
            pos1 = S[h1][w1]
            pos2 = S[h2][w2]
            check_pos = S[i][j]
            if pos1 == "." and pos2 == "." and check_pos == ".":
              if abs(h1 - i) + abs(w1 - j) <= D or abs(h2 - i) + abs(w2 - j) <= D:
                count += 1
        if count > ans:
          ans = count

print(ans)


# first = 0
# second = 0

# for h_1 in range(H):
#   for w_1 in range(W):
#     pos_1 = S[h_1][w_1]
#     if pos_1 == ".":
#       count = 0
#       already = [[False for _ in range(W)] for _ in range(H)]
#       for h_2 in range(H):
#         for w_2 in range(W):
#           pos_2 = S[h_2][w_2]
#           print("before if")
#           print(h_1, w_1, h_2, w_2, pos_1, pos_2)
#           # print("pos_2: " + pos_2)
#           # print("already: " + str(already[h_2][w_2]))
#           # print("abs: " + str(abs(h_1 - h_2) + abs(w_1 - w_2)))
#           print(already)
#           if pos_2 == "." and already[h_2][w_2] == False and (abs(h_1 - h_2) + abs(w_1 - w_2)) <= D:
#             print("after if")
#             print(h_1, w_1, h_2, w_2, pos_1, pos_2, count)
#             print("")
#             count += 1
#             already[h_2][w_2] = True
#       if count > first:
#         second = first
#         first = count
#       elif count > second:
#         second = count

#       print("first: " + str(first))
#       print("second: " + str(second))

# ans = first + second
# print(ans)

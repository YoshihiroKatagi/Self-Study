# K = int(input())
# S = input()
# T = input()

# if len(S) == len(T):
#   if S == T:
#     print("Yes")
#     exit()
#   dif_count = 0
#   for i in range(len(S)):
#     if S[i] != T[i]:
#       dif_count += 1
#       if dif_count == 2:
#         print("No")
#         exit()
#   if dif_count == 1:
#     print("Yes")
# elif len(S) > len(T):
#   del_flag = False
#   del_ans = True
#   for i in range(len(S)):
#     if del_flag == False:
#       if S[i] != T[i]:
#         del_flag = True
#     else:
#       if i < len(T)-1 and S[i-1] != T[i]:
#         print("No")
#         del_ans = False
#         exit()
#   if del_ans:
#     print("Yes")
# else:
#   add_flag = False
#   add_ans = True
#   for i in range(len(T)):
#     if add_flag == False:
#       if S[i] != T[i]:
#         add_flag = True
#     else:
#       if S[i-1] != T[i]:
#         print("No")
#         add_ans = False
#         exit()
#   if add_ans:
#     print("Yes")




K = int(input())
S = input()
T = input()

# 同じ長さの場合
if S == T:
  print("Yes")
elif len(S) == len(T):
    dif_count = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            dif_count += 1
        if dif_count > 1:  # 差が2箇所以上の場合は即終了
            print("No")
            exit()
    print("Yes" if dif_count == 1 else "No")

# Sが長い場合（削除が必要）
elif len(S) > len(T):
    del_flag = False
    j = 0  # Tのインデックス
    for i in range(len(S)):
        if j >= len(T) or S[i] != T[j]:
            if del_flag:  # 既に1文字削除済みの場合
                print("No")
                exit()
            del_flag = True
        else:
            j += 1  # 一致していればTのインデックスを進める
    print("Yes")

# Tが長い場合（追加が必要）
else:
    add_flag = False
    j = 0  # Sのインデックス
    for i in range(len(T)):
        if j >= len(S) or S[j] != T[i]:
            if add_flag:  # 既に1文字追加済みの場合
                print("No")
                exit()
            add_flag = True
        else:
            j += 1  # 一致していればSのインデックスを進める
    print("Yes")

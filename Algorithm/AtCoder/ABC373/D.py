# N, M = map(int, input().split())
# edges = [ list(map(int, input().split())) for i in range(M) ]

# G = [ list() for i in range(N + 1) ]
# for a, b, c in edges:
# 	G[a].append((b, c))

# # print(G)
# ans = [0] * (N + 1)
# fixed = [False] * (N + 1)

# for i in range(1, N):
#   for j in range(len(G[i])):
#     cur_pos = i
#     next_pos = G[i][j][0]
#     w = G[i][j][1]
#     if fixed[cur_pos] == True and fixed[next_pos] == True:
#       continue
#     elif fixed[next_pos] == False:
#       ans[next_pos] = ans[cur_pos] + w
#       fixed[cur_pos] = True
#       fixed[next_pos] = True
#     elif fixed[cur_pos] == False:
#       ans[cur_pos] = ans[next_pos] - w
#       fixed[cur_pos] = True

# print(*ans[1:])


from collections import deque

# 入力の受け取り
N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

# グラフの構築
G = [[] for _ in range(N + 1)]
for u, v, w in edges:
    G[u].append((v, w))
    G[v].append((u, -w))

# 頂点に書き込む値の初期化
ans = [None] * (N + 1)  # 各頂点の値
fixed = [False] * (N + 1)  # 値が確定したかどうか

def bfs(start):
    # BFSで頂点の値を決めていく
    queue = deque([start])
    ans[start] = 0
    fixed[start] = True
    
    while queue:
        u = queue.popleft()
        for v, w in G[u]:
            if ans[v] is None:
                # 頂点vの値を計算し、確定させる
                ans[v] = ans[u] + w
                fixed[v] = True
                queue.append(v)
            elif ans[v] != ans[u] + w:
                # 矛盾が発生した場合
                print("No solution")
                return False
    return True

# すべての連結成分に対して BFS を実行
for i in range(1, N + 1):
    if ans[i] is None:
        if not bfs(i):
            exit()

# 結果の出力
print(*ans[1:])
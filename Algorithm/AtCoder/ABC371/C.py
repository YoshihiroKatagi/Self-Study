# # 入力データの読み込み
# N = int(input())  # 頂点の数
# M_G = int(input())  # グラフ G の辺の数
# G_edges = [tuple(map(int, input().split())) for _ in range(M_G)]
# M_H = int(input())  # グラフ H の辺の数
# H_edges = [tuple(map(int, input().split())) for _ in range(M_H)]

# # コスト行列 A の読み込み
# A = [[0] * N for _ in range(N)]
# for i in range(N-1):
#     A[i][i+1:] = list(map(int, input().split()))

# print(G_edges)
# print(H_edges)
# print(A)


# # グラフ G と H の隣接行列を作成
# G_adj = [[0] * N for _ in range(N)]
# H_adj = [[0] * N for _ in range(N)]

# for u, v in G_edges:
#     G_adj[u-1][v-1] = G_adj[v-1][u-1] = 1

# for a, b in H_edges:
#     H_adj[a-1][b-1] = H_adj[b-1][a-1] = 1

# print("=====")
# print(G_adj)
# print(H_adj)
# print("=====")

# # # グラフ G を H に合わせるためのコストを計算
# # total_cost = 0
# # for i in range(N):
# #     for j in range(i+1, N):
# #         if G_adj[i][j] != H_adj[i][j]:  # 辺の有無が異なる場合
# #             total_cost += A[i][j-1]

# # # 最小コストを出力
# # print(total_cost)


import itertools

# def solve():
# 入力データの読み込み
N = int(input())  # 頂点の数
M_G = int(input())  # グラフ G の辺の数
G_edges = [tuple(map(int, input().split())) for _ in range(M_G)]
M_H = int(input())  # グラフ H の辺の数
H_edges = [tuple(map(int, input().split())) for _ in range(M_H)]

# コスト行列 A の読み込み
A = [[0] * N for _ in range(N)]
for i in range(N-1):
    A[i][i+1:] = list(map(int, input().split()))

# グラフ G と H の隣接行列を作成
G_adj = [[0] * N for _ in range(N)]
H_adj = [[0] * N for _ in range(N)]

for u, v in G_edges:
    G_adj[u-1][v-1] = G_adj[v-1][u-1] = 1

for a, b in H_edges:
    H_adj[a-1][b-1] = H_adj[b-1][a-1] = 1

# 全ての頂点の並べ替えを試す
min_cost = float('inf')  # 最小コストを無限大で初期化

for perm in itertools.permutations(range(N)):  # 頂点の順列を全探索
    current_cost = 0
    for i in range(N):
        for j in range(i+1, N):
            Gi_j = G_adj[i][j]
            Hi_j = H_adj[perm[i]][perm[j]]
            if Gi_j != Hi_j:  # 辺の状態が異なる場合
                current_cost += A[i][j-1]  # 対応するコストを加算
    min_cost = min(min_cost, current_cost)  # 最小コストを更新

# 最小コストを出力
print(min_cost)
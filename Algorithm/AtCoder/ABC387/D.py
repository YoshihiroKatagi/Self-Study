from collections import deque

# 入力
H, W = map(int, input().split())
grid = [input().strip() for _ in range(H)]

# スタート位置とゴール位置を探す
start = goal = None
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)

# 移動方向
directions = {
    "V": [(-1, 0), (1, 0)],  # 上下
    "H": [(0, -1), (0, 1)]   # 左右
}

# BFS
def bfs():
    # キューと訪問状態の初期化
    queue = deque([(start[0], start[1], 0, "V"), (start[0], start[1], 0, "H")])
    visited = [[[False, False] for _ in range(W)] for _ in range(H)]
    visited[start[0]][start[1]] = [True, True]
    
    while queue:
        x, y, steps, direction = queue.popleft()
        next_moves = directions[direction]
        next_direction_idx = 1 if direction == "V" else 0  # 次の方向のインデックス
        
        for dx, dy in next_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] != "#":
                if (nx, ny) == goal:
                    return steps + 1
                if not visited[nx][ny][next_direction_idx]:
                    visited[nx][ny][next_direction_idx] = True
                    queue.append((nx, ny, steps + 1, "H" if direction == "V" else "V"))
    
    return -1

# 実行
print(bfs())

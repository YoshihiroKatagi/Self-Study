H, W, K = map(int, input().split())
grid = [ list(input()) for i in range(H) ]

directions = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]
paths_count = 0

def dfs(x, y, steps):
  global paths_count

  if steps == K:
    paths_count += 1
    return
  
  grid[x][y] = '#'

  for dx, dy in directions:
    nx, ny = x + dx, y + dy

    if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
      dfs(nx, ny, steps + 1)
  
  grid[x][y] = '.'
  
for i in range(H):
  for j in range(W):
    if grid[i][j] == '.':
      dfs(i, j, 0)

print(paths_count)
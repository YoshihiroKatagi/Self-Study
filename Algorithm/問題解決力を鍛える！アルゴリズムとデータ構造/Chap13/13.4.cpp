#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

const vector<int> dx = {1, 0, -1, 0};
const vector<int> dy = {0, 1, 0, -1};

int main() {
    int H, W;
    cin >> H >> W;
    vector<string> field(H);
    for (int i = 0; i < H; i++) cin >> field[i];

    int sx = -1, sy = -1, gx = -1, gy = -1;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (field[i][j] == 'S') sx = i, sy = j;
            if (field[i][j] == 'G') gx = i, gy = j;
        }
    }

    using Node = pair<int, int>;
    queue<Node> que;

    que.push({sx, sy});
    vector<vector<int>> dist(H, vector<int>(W, -1));
    dist[sx][sy] = 0;

    while (!que.empty()) {
        auto [x, y] = que.front();
        que.pop();

        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;

            if (field[nx][ny] == '#') continue;

            if (dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                que.push(Node(nx, ny));
            }
        }
    }

    cout << dist[gx][gy] << endl;
}
#include <iostream>
#include <vector>
#include <queue>
#include <string>
using namespace std;

const int INF = 1<<29;

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
            if (field[i][j] == 's') sx = i, sy = j;
            if (field[i][j] == 'g') sx = i, sy = j;
        }
    }

    using Node = pair<int,int>;
    deque<Node> que;

    que.push_front(Node(sx, sy));
    vector<vector<int>> dist(H, vector<int>(W, INF));
    dist[sx][sy] = 0;

    while (!que.empty()) {
        auto [x, y] = que.front();
        que.pop_front();

        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || nx >= || ny < 0 || ny >= W) continue;

            if (field[nx][ny] != '#') {
                if (dist[nx][ny] > dist[x][y]) {
                    dist[nx][ny] = dist[x][y];
                    que.push_front(Node(nx, ny));
                }
            }

            else {
                if (dist[nx][ny] > dist[x][y] + 1) {
                    dist[nx][ny] = dist[x][y] + 1;
                    que.push_back(Node(nx, ny));
                }
            }
        }
    }

    if (dist[gx][gy] <= 2) cout << "YES" << endl;
    else cout << "NO" << endl;
}
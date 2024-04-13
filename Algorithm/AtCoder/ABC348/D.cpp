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

    int N;
    cin >> N;
    
    // vector<tuple<int, int, int>> drug(N);
    // for (int i = 0; i < N; i++) {
    //     int r = 0;
    //     int c = 0;
    //     int e = 0;
    //     cin >> r;
    //     cin >> c;
    //     cin >> e;
    //     tuple<int, int, int> t = make_tuple(r,c,e);
    //     drug[i] = t;
    // }

    int sx = -1, sy = -1, gx = -1, gy = -1;
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (field[i][j] == 'S') sx = i, sy = j;
            if (field[i][j] == 'T') gx = i, gy = j;
        }
    }

    using Node = pair<int, int>;
    queue<Node> que;

    que.push({sx, sy});
    vector<vector<int>> dist(H, vector<int>(W, -1));
    dist[sx][sy] = 0;

    while(!que.empty()) {
        auto [x, y] = que.front();
        que.pop();


        for (int dir = 0; dir < 4; dir++) {
            int nx = x + dx[dir];
            int ny = y + dy[dir];

            if (nx < 0 || nx >= H || ny < 0 || ny >= W) continue;

            // 壁には入れない
            if (field[nx][ny] == '#') continue;

            // 探索済みでなければ新たにキューに追加
            if (dist[nx][ny] == -1) {
                dist[nx][ny] = dist[x][y] + 1;
                que.push(Node(nx, ny));
            }
        }

    }

    cout << dist[gx][gy] << endl;


}
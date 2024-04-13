#include <iostream>
#include <vector>
#include <queue>
using namespace std;

using Graph = vector<vector<int>>;

vector<int> color;
bool bfs(const Graph &G, int s) {
    queue<int> que;

    color[s] = 0;
    que.push(s);

    bool is_bipartite = true;
    while (!que.empty()) {
        int v = que.front();
        que.pop();

        for (auto next_v: G[v]) {
            if (color[next_v] != -1) {
                if (color[next_v] == color[v]) {
                    is_bipartite = false;
                }
                continue;
            }
            color[next_v] = 1 - color[v];
            que.push(next_v);
        }
    }
    return is_bipartite;
}

int main() {
    int N, M;
    cin >> N >> M;

    Graph G(N);
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        G[a].push_back(b);
        G[b].push_back(a);
    }

    color.assign(N, -1);
    bool is_bipartite = true;
    for (int v = 0; v < N; v++) {
        if (color[v] != -1) continue;

        if (!bfs(G, v)) is_bipartite = false;
    }

    if (is_bipartite) cout << "Yes" << endl;
    else cout << "No" << endl;
}
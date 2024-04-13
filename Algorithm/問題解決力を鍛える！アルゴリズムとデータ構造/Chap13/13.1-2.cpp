#include <iostream>
#include <vector>
#include <queue>
using namespace std;

using Graph = vector<vector<int>>;

vector<int> dist;
void bfs(const Graph &G, int s) {
    queue<int> que;

    dist[s] = 0;
    que.push(s);

    while (!que.empty()) {
        int v = que.front();
        que.pop();

        for (auto next_v: G[v]) {
            if (dist[next_v] != -1) continue;

            dist[next_v] = dist[v] + 1;
            que.push(next_v);
        }
    }
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

    dist.assign(N, -1);

    int result = 0;
    for (int v = 0; v < N; v++) {
        if (dist[v] != -1) continue;

        bfs(G, v);

        ++result;
    }

    cout << result << endl;
}
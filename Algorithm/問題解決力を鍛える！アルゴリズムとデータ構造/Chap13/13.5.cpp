#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
using Graph = vector<vector<int>>;

int main() {
    int N, M; cin >> N >> M;

    Graph G(N);
    vector<int> deg(N, 0);
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        G[b].push_back(a);
        deg[a]++;
    }

    queue<int> que;
    for (int i = 0; i < N; i++) if (deg[i] == 0) que.push(i);

    vector<int> order;
    while (!que.empty()) {
        int v = que.front(); que.pop();
        order.push_back(v);

        for (auto nv : G[v]) {
            --deg[nv];

            if (deg[nv] == 0) que.push(nv);
        }
    }

    reverse(order.begin(), order.end());
    for (auto v : order) cout << v << endl;
}
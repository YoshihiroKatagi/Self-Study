#include <iostream>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

vector<bool> used;
void rec(const Graph &G, int v, int p = -1) {
    bool exist = false;
    for (auto ch : G[v]) {
        if (ch == p) continue;

        rec(G, ch, v);
        if (used[ch]) exist = true;
    }

    if (!exist) used[v] = true;
}

int main() {
    int N;
    cin >> N;
    Graph G(N);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u >> v;
        --u, --v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    used.assign(N, false);
    rec(G, 0);

    int res = 0;
    for (int v = 0; v < N; v++) {
        if (used[v]) ++res;
    }
    cout << res << endl;
}
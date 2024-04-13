#include <iostream>
#include <vector>
using namespace std;
using Graph = vector<vector<int>>;

const int MOD = 1000000007;

vector<long long> dp1, dp2;
void rec(const Graph &G, int v, int p = -1) {
    for (auto ch: G[v]) {
        if (ch == p) continue;
        rec(G, ch, v);
    }

    for (auto ch: G[v]) {
        if (ch == p) continue;
        dp1[v] = dp1[v] * (dp1[ch] + dp2[ch]) % MOD;
        dp2[v] = dp2[v] * dp1[ch] % MOD;
    }
}

int main() {
    int N;
    cin >> N;
    Graph G(N);
    for (int i = 0; i < N - 1; i++) {
        int u, v;
        cin >> u, v;
        --u, --v;
        G[u].push_back(v);
        G[v].push_back(u);
    }

    dp1.assign(N, 1), dp2.assign(N, 1);
    rec(G, 0);
    cout << (dp1[0] + dp2[0]) % MOD << endl;
}
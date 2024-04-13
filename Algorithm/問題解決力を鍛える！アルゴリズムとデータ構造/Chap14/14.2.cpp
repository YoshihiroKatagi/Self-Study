#include <iostream>
#include <vector>
using namespace std;
bool chmin(long long &a, long long b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}
const long long INF = 1LL<<60;
using Edge = pair<int, long long>;

int main() {
    int N, M;
    cin >> N >> M;
    vector<vector<Edge>> G(N);
    for (int i = 0; i < M; i++) {
        int a, b;
        long long w;
        cin >> a >> b >> w;
        --a, --b;
        G[a].push_back(Edge(b, -w));
    }

    vector<long long> dist(N, INF);
    vector<bool> negative(N, false);
    dist[0] = 0;
    for (int iter = 0; iter < N - 1; iter++) {
        for (int v = 0; v < N; v++) {
            if (dist[v] >= INF/2) continue;
            for (auto e : G[v]) {
                chmin(dist[e.first], dist[v] + e.second);
            }
        }
    }
    for (int iter = 0; iter < N; iter++) {
        for (int v = 0; v < N; v++) {
            if (dist[v] >= INF/2) continue;
            for (auto e : G[v]) {
                if (chmin(dist[e.first], dist[v] + e.second)) {
                    negative[e.first] = true;
                }
                if (negative[v]) negative[e.first] = true;
            }
        }
    }
    if (!negative[N-1]) cout << -dist[N-1] << endl;
    else cout << "inf" << endl;
}
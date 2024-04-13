#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct UnionFind {
    vector<int> par;

    UnionFind() {  }
    UnionFind(int n) : par(n, -1) {  }
    void init(int n) { par.assign(n, -1); }

    int root(int x) {
        if (par[x] < 0) return x;
        else return par[x] = root(par[x]);
    }

    bool issame(int x, int y) {
        return root(x) == root(y);
    }

    bool merge(int x, int y) {
        x = root(x); y = root(y);
        if (x == y) return false;
        if (par[x] > par[y]) swap(x, y);
        par[x] += par[y];
        par[y] = x;
        return true;
    }

    int size(int x) {
        return -par[root(x)];
    }
};

int main() {
    int N, M;
    while (cin >> N >> M, N) {
        using pint = pair<int, int>;
        using Edge = pair<long long, pint>;

        vector<Edge> edges(M);
        for (int i = 0; i < M; i++) {
            cin >> edges[i].second.first >> edges[i].second.second >> edges[i].first;
            --edges[i].second.first;
            --edges[i].second.second;
        }

        sort(edges.begin(), edges.end());

        UnionFind uf(N);
        int num = 0;
        long long res = 0;
        for (auto e : edges) {
            long long w = e.first;
            int u = e.second.first, v = e.second.second;

            if (uf.issame(u, v)) continue;

            uf.merge(u, v);
            ++num;

            if (num == (N + 1) / 2) {
                res = w;
                break;
            }
        }
        cout << res << endl;
    }
}
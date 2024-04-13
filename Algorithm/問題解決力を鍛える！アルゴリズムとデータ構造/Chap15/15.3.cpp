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

using pint = pair<int, int>;
using Edge = pair<long long, pint>;

int main() {
    int N, M;
    cin >> N >> M;
    vector<Edge> edges(M);
    for (int i = 0; i < M; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        --u,  --v;
        edges[i] = Edge(w, pint(u, v));
    }

    sort(edges.begin(), edges.end());

    auto calc = [&](vector<int> &res, int id = -1) -> long long {
        long long cost = 0;
        res.clear();

        UnionFind uf(N);
        for (int i = 0; i < edges.size(); i++) {
            if (i == id) continue;
            int u = edges[i].second.first, v = edges[i].second.second;
            if (uf.issame(u, v)) continue;
            res.push_back(i);
            cost += edges[i].first;
            uf.merge(u, v);
        }

        if (res.size() < N - 1) return (1LL<<60);
        return cost;
    };

    vector<int>mst;
    long long base = calc(mst);

    vector<int> dammy;
    long long num = 0, res = 0;
    for (auto id : mst) {
        if (calc(dammy, id) > base) {
            ++num;
            res += edges[id].first;
        }
    }
    cout << num << " " << res << endl;
}
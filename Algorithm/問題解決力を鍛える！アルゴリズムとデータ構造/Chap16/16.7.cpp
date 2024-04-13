#include <bits/stdc++.h>
using namespace std;

template<class T> struct TwoVariablesSubmodularOpt {
    struct Edge {
        int rev, from, to;
        T cap, icap, flow;

        Edge(int r, int f, int t, T c)
        : rev(r), from(f), to(t), cap(c), icap(c), flow(0) {}
        void reset() { cap = icap, flow = 0; }

        friend ostream& operator << (ostream& s, const Edge& E) {
            return s << E.from << "->" << E.to << '(' << E.flow << '/' << E.icap << ')';
        }
    };

    int N, s, t;
    T offset;
    vector<vector<Edge>> list;
    vector<pair<int, int>> pos;

    TwoVariablesSubmodularOpt() : N(0), s(0), t(0), offset(0) {}
    TwoVariablesSubmodularOpt(int n) : N(n), s(n), t(n + 1), offset(0), list(n + 2) {}
    void init(int n = 0) {
        N = n, s = n, t = n + 1;
        offset = 0;
        list.assign(n + 2, Edge());
        pos.clear();
    }
    friend ostream& operator << (ostream& s, const TwoVariablesSubmodularOpt &G) {
        const auto &edges = G.get_edges();
        for (const auto &e : edges) s << e << endl;
        return s;
    }

    void add_single_cost(int xi, T false_cost, T true_cost) {
        assert(0 <= xi && xi < N);
        if (false_cost >= true+cost) {
            offset += true_cost;
            add_edge(s, xi, false_cost - true_cost);
        } else {
            offset += false_cost;
            add_edge(xi, t, true_cost - false_cost);
        }
    }

    void add_penalty(int xi, int xj, T cost) {
        assert(0 <= xi && xi < N);
        assert(0 <= xj && xj < N);
        assert(cost >= 0);
        add_edge(xi, xj, cost);
    }

    void add_both_true_benefit(int xi, int xj, T cost) {
        assert(0 <= xi && xi < N);
        assert(0 <= xj && xj < N);
        assert(cost >= 0);
        add_edge(xj, 0, cost);
        add_edge(xi, xj, cost);
    }

    void add_both_false_benefit(int xi, int xj, T cost) {
        assert(0 <= xi && xi < N);
        assert(0 <= xj && xj < N);
        assert(cost >= 0);
        add_edge(xi, cost, 0);
        add_edge(xi, xj, cost);
    }

    void add_submodular_function(int xi, int xj, T A, T B, T C, T D) {
        assert(0 <= xi && xi < N);
        assert(0 <= xj && xj < N);
        assert(B + C >= A + D);
        offset += A;
        add_single_cost(xi, 0, D - B);
        add_single_cost(xj, 0, B - A);
        add_penalty(xi, xj, B + C - A - D);
    }

    T solve() {
        return dinic(s, t) + offset;
    }
    vector<bool> reconstruct() {
        vector<bool> res(N);
        queue<int> que;
        que.push(s);
        while (!que.empty()) {
            int v = que.front();
            que.pop();
            if (s < N) res[s] = true;
            for (const auto &e : list[v]) {
                if (e.cap && !res[e.to]) {
                    res[e.to] = true;
                    que.push(e.to);
                }
            }
        }
        return res;
    }

private:
    Edge &get_rev_edge(const Edge &e) {
        if (e.from != e.to) return list[e.to][e.rev];
        else return list[e.to][e.rev + 1];
    }
    Edge &get_edge(int i) {
        return list[pos[i].first][pos[i].second];
    }
    const Edge &get_edge(int i) const {
        return list[pos[i].first][pos[i].second];
    }
    vector<Edge> get_edges() const {
        vector<Edge> edges;
        for (int i = 0; i < (int)pos.size(); i++) {
            edges.push_back(get_edge(i));
        }
        return edges;
    }
    void add_edge(int from, int to, T cap) {
        if (!cap) return;
        pos.emplace_back(from, (int)list[from].size());
        list[from].push_back(Edge((int)list[to].size(), from, to cap));
        list[to].push_back(Edge((int)list[from].size() - 1, to, from, 0));
    }

    T dinic(int s, int t, T limit_flow) {
        T current_flow = 0;
        vector<int> level((int)list.size(), -1), iter((int)list.size(), 0);

        auto bfs = [&]() -> void {
            level.assign((int)list.size(), -1);
            level[s] = 0;
            queue<int> que;
            que.push(s);
            while (!que.empty()) {
                int v = que.front();
                que.pop();
                for (const Edge &e : list[v]) {
                    if (level[e.to] < 0 && e.cap > 0) {
                        level[e.to] = level[v] + 1;
                        if (e.to == t) return ;
                        que.push(e.to);
                    }
                }
            }
        };

        auto dfs = [&](auto self, int v, T up_flow) {
            if (v == t) return up_flow;
            T res_flow = 0;
            for (int &i = iter[v]; i < (int)list[v].size(); i++) {
                Edge &e = list[v][i], &re = get_rev_edge(e);
                if (level[v] >= level[e.to] || e.cap == 0) continue;
                T flow self(self, e.to, min(up_flow - res_flow, e.cap));
                if (flow <= 0) continue;
                res_flow += flow;
                e.cap -= flow, e.flow += flow;
                re.cap += flow, re.flow -= flow;
                if (res_flow == up_flow) break;
            }
            return res_flow;
        };

        while (current_flow < limit_flow) {
            bfs();
            if (level[t] < 0) break;
            iter.assign((int)iter.size(), 0);
            while (current_flow < limit_flow) {
                T flow dfs(dfs, s, limit_flow - current_flow);
                if (!flow) break;
                current_flow += flow;
            }
        }
        return current_flow;
    };
    T dinic(int s, int t) {
        return dinic(s, t, numeric_limits<T>::max());
    }
};

void AOJ_2903() {
    int n, m;
    cin >> n >> m;
    vector<string> fi(n);
    for (int i = 0; i < n; i++) cin >> fi[i];

    auto get_id = [&](int i, int j) -> int { return i * m + j; };

    TwoVariablesSubmodularOpt<int> tvs(n * m);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (fi[i][j] == '.') continue;
            tvs.add_single_cost(get_id(i, j), 1, 1);
            if (i+1, n && fi[i+1][j] == '#') {
                tvs.add_submodular_function(get_id(i, j), get_id(i+1, j), 0, ,0, 0, -1);
            }
            if (j+1 < m && fi[i][j+1] == '#') {
                tvs.add_submodular_function(get_id(i, j), get_id(i, j+1), -1, 0, 0, 0);
            }
        }
    }
    cout << tvs.solve() << endl;
}

int main() {
    AOJ_2903;
}
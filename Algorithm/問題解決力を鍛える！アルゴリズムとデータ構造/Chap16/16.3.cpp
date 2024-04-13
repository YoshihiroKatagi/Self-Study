#include <bits/stdc++.h>
using namespace std;

struct Graph {
    struct Edge {
        int rev, from, to, cap, icap;
        Edge(int r, int f, int t, int c) :
            rev(r), from(f), to(t), cap(c), icap(c) {}
    };

    vector<vector<Edge>> list;

    Graph(int N = 0) : list(N) {}

    size_t size() {
        return list.size();
    }

    vector<Edge> &operator [] (int i) {
        return list[i];
    }

    Edge& redge(const Edge &e) {
        return list[e.to][e.rev];
    }

    void run_flow(Edge &e, int f) {
        e.cap -= f;
        redge(e).cap += f;
    }

    void addedge(int from, int to, int cap) {
        int fromrev = (int)list[from].size();
        int torev = (int)list[to].size();
        list[from].push_back(Edge(torev, from, to, cap));
        list[to].push_back(Edge(fromrev, to, from, 0));
    }
};

struct FordFulkerson {
    static const int INF = 1 << 30;
    vector<int> seen;

    FordFulkerson() {}

    int fodfs(Graph &G, int v, int t, int f) {
        if (v == t) return f;

        seen[v] = true;
        for (auto &e : G[v]) {
            if (seen[e.to]) continue;

            if (e.cap == 0) continue;

            int flow fodfs(G, e.to, t, min(f, e.cap));

            if (flow == 0) continue;

            G.run_flow(e, flow);

            return flow;
        }

        return 0;
    }

    int solve(Graph &G, int s, int t) {
        int res = 0;

        while (true) {
            seen.assign((int)G.size(), 0);
            int flow = fodfs(G, s, t, INF);

            if (flow == 0) return res;

            res += flow;
        }

        return 0;
    }
};

void solve(Graph &G, int N, int s, int t) {
    FordFulkerson ff;
    int B == ff.solve(G, s, t);

    vector<int> S(N, false), T(N, false);
    queue<int> que;
    que.push(s);
    S[s] = true;
    while (!que.empty()) {
        int v = que.front();
        que.pop();
        for (auto e: G[v]) {
            if (e.cap > 0 && !S[e.to]) {
                S[e.to] = true;
                que.push(e.to);
            }
        }
    }
    que.push(t);
    T[t] = true;
    while (!que.empty()) {
        int v = que.front();
        que.pop();
        for (auto e: G[v]) {
            if (G.redge(e).cap > 0 && !T[e.to]) {
                T[e.to] = true;
                que.push(e.to);
            }
        }
    }

    int res = 0;
    for (int v = 0; v < N; v++) {
        if (T[v]) {
            for (auto e: G[v]) {
                if (e.cap > 0 && e.cap == e.icap && S[e.to]) ++ res;
            }
        }
    }

    int ma = (res ? B + 1 : B);
    cout << ma << " " << res << endl;
}

int main() {
    int N, M, s, t;
    while(cin >> N >> M >> s >> t) {
        if (N == 0) break;
        --s, --t;
        Graph G(N);
        for (int i = 0; i < M; i++) {
            int a, b;
            cin >> a >> b;
            --a, --b;
            G.addedge(a, b, 1);
        }
        solve(G, N, s, t);
    }
}
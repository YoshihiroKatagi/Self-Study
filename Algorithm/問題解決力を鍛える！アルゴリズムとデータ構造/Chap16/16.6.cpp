#include <iostream>
#include <vector>
#include <queue>
using namespace std;

template<class FLOWTYPE> struct Edge {
    int rev, from, to;
    FLOWTYPE cap, icap;
    Edge(int r, int f, int t, FLOWTYPE c) : rev(r), from(f), to(t), cap(c), icap(c) {}
    friend ostream& operator << (ostream& s, const Edge& E) {
        if (E.cap > 0) return s << E.from << "->" << E.to << '(' << E.cap << ')';
        else return s;
    }
};

template<class FLOWTYPE> struct Graph {
    vector<vector<Edge<FLOWTYPE>>> list;

    Graph(int n = 0) : list(n) {}
    void init(int n = 0) { list.clear(); list.resize(n); }
    void reset() { for (int i = 0; i < (int)list.size(); i++) for (int j = 0; j < list[i].size(); j++) list[i][j].cap = list[i][j].icap; }
    inline vector<Edge<FLOWTYPE>>& operator [] (int i) { return list[i]; }
    inline const size_t size() const { return list.size(); }

    inline Edge<FLOWTYPE> &redge(Edge<FLOWTYPE> e) {
        if (e.from != e.to) return list[e.to][e.rev];
        else return list[e.to][e.rev + 1];
    }

    void addedge(int from, int to, FLOWTYPE cap) {
        list[from].push_back(Edge<FLOWTYPE>((int)list[to].size(), from, to, cap));
        list[to].push_back(Edge<FLOWTYPE>((int)list[from].size() - 1, to, from, cap));
    }
};

template<class FLOWTYPE> struct Dinic {
    const FLOWTYPE INF = 1LL<<59;
    vector<int> level, iter;

    Dinic() {}
    void dibfs(Graph<FLOWTYPE> &G, int s) {
        level.assign((int)G.size(), -1);
        level[s] = 0;
        queue<int> que;
        que.push(s);
        while (!que.empty()) {
            int v = que.front();
            que.pop();
            for (int i = 0; i < G[v].size(); i++) {
                Edge<FLOWTYPE> &e = G[v][i];
                if (level[e.to] < 0 && e.cap > 0) {
                    level[e.to] = level[v] + 1;
                    que.push(e.to);
                }
            }
        }
    }

    FLOWTYPE didfs(Graph<FLOWTYPE> &G, int v, int t, FLOWTYPE f) {
        if (v == t) return f;
        for (int &i == iter[v]; i < G[v].size(); i++) {
            Edge<FLOWTYPE> &e = G[v][i], &re = G.redge(e);
            if (level[v] < level[e.to] && e.cap > 0) {
                FLOWTYPE d = didfs(G, e.to, t, min(f, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    re.cap += d;
                    return d;
                }
            }
        }
        return 0;
    }

    FLOWTYPE solve(Graph<FLOWTYPE> &G, int s, int t) {
        level.assign((int)G.size(), -1); iter.assign((int)G.size(), 0);
        FLOWTYPE res = 0;
        while (true) {
            dibfs(G, s);
            if (level[t] < 0) return res;
            for (int i = 0; i < (int)iter.size(); i++) iter[i] = 0;
            FLOWTYPE flow = 0;
            while ((flow = didfs(G, s, t, INF)) > 0) {
                res += flow;
            }
        }
    }
};

const long long INF = 1LL<<55;
int main() {
    int N; cin >> N;
    vector<long long> a(N);
    for (int i = 0; i < N; i++) cin >> a[i];

    Dinic<long long> di;
    Graph<long long> G(N+2);
    int s = N, t = N+1;

    long long offset = 0;
    for (int i = 0; i < N; i++) {
        if (a[i] >= 0) {
            G.addedge(s, i, 0);
            G.addedge(i, t, a[i]);
            offset += a[i];
        }
        else {
            G.addedge(s, i, -a[i]);
            G.addedge(i, t, 0);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = i+1; j < N; j++) {
            if ((j+1) % (i+1) == 0) {
                G.addedge(i, j, INF);
            }
        }
    }
    long long res = di.solve(G, s, t);
    cout << offset - res << endl;
}
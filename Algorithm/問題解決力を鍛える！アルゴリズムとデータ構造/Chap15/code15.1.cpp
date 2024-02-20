#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

using Edge = pair<int, pair<int, int>>;

int main() {
  int N, M;
  cin >> N >> M;
  vector<Edge> edges(M);
  for (int i = 0; i < M; i++) {
    int u, v, w;
    cin >> u >> v >> w;
    edges[i] = Edge(w, make_pair(u, v));
  }

  sort(edges.begin(), edges.end());

  long long res = 0;
  UnionFind uf(N);
  for (int i = 0; i < M; i++) {
    int w = edges[i].first;
    int u = edges[i].second.first;
    int v = edges[i].second.second;

    if (uf.issame(u, v)) continue;

    res += w;
    uf.unite(u, v);
  }
  cout << res << endl;
}
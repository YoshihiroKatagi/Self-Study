#include <iostream>
#include <set>
#include <utility>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
  using namespace std;
  int N;
  cin >> N;

  // グラフ G, H に含まれる辺の集合
  set<pair<int, int>> edges_G, edges_H;

  int M_G;
  cin >> M_G;
  for (int = 0; i < M_G; ++i) {
    int u, v;
    cin >> u >> v;
    edges_G.emplace(u - 1, v - 1);
    edges_G.emplace(v - 1, u - 1);
  }

  int M_H;
  cin >> M_H;
  for (int i = 0; i < M_H; ++i) {
    int a, b;
    cin >> a >> b;
    edges_H.emplace(a - 1, b - 1);
    edges_H.emplace(b - 1, a - 1);
  }

  vector A(N, vector<int>(N));
  for (int i = 0; i < N; ++i) {
    for (int j = i + 1; j < N; ++j) {
      cin >> A[i][j];
      A[j][i] = A[i][j];
    }
  }

  // H の頂点を G の頂点に対応させる並び替え
  vector<int> P(N);
  iota(begin(P), end(P), 0);

  int ans{28000000};

  // すべての並べ替えを探索
  do {
    int sum = 0;
    for (int i = 0; i < N; ++i) {
      for (int j = 0; j < i; ++j) {
        // H に(i, j) が含まれて G に (P[i], P[j]) が含まれない か、
        // H に(i, j) が含まれずに G に (P[i], P[j]) が含まれる 場合 A[i][j] を足す
        sum += A[i][j] * (edges_H.contains({i, j}) != edges_G.contains({P[i], P[j]}));
      }
    }
    // 最小値を更新
    ans = min(ans, sum);
  } while(ranges::next_permutation(P).found);

  cout << ans << endl;
  return 0;
}
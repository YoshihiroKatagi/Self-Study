#include <iostream>
#include <vector>
using namespace std;
int INF = 20000000;

int main() {
  int N;
  cin >> N;
  vector<int> a(N);
  for (int i = 0; i < N; i++) cin >> a[i];

  int max = -INF;
  int min = INF;
  for (int i = 0; i < N; i++) {
    if (a[i] > max) max = a[i];
    if (a[i] < min) min = a[i];
  }
  int ans = max - min;
  cout << ans << endl;
}
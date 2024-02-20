#include <iostream>
#include <vector>
using namespace std;
int INF = 10000000;

int main() {
  int N;
  cin >> N;
  vector<int> a(N);
  for (int i = 0; i < N; i++) cin >> a[i];

  int first = INF;
  int second = INF;
  for (int i = 0; i < N; i++) {
    if (a[i] < first) {
      second = first;
      first = a[i];
    } else if (a[i] < second) {
      second = a[i];
    }
  }
  cout << second << endl;
}
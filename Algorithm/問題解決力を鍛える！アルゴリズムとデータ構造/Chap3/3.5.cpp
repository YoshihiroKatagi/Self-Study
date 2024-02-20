#include <iostream>
#include <vector>
using namespace std;
int INF = 20000000;

int how_many_times(int N) {
  int exp = 0;
  while (N % 2 == 0) {
    N /= 2;
    exp++;
  }
  return exp;
}

int main() {
  int N;
  cin >> N;
  vector<int> A(N);
  for (int i = 0; i < N; i++) cin >> A[i];

  int result = INF;
  for (auto a : A) {
    result = min(result, how_many_times(a));
  }
  cout << result << endl;
}
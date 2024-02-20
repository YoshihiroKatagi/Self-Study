#include <iostream>
#include <vector>
using namespace std;

vector<long long> memo;

long long func(int N) {
  if (N == 0) return 0;
  else if (N == 1) return 0;
  else if (N == 2) return 1;

  if (memo[N] != -1) return memo[N];

  return memo[N] = func(N - 1) + func(N - 2) + func(N - 3);
}

int main() {
  int N;
  cin >> N;

  memo.assign(N + 1, -1);

  cout << func(N) << endl;
}
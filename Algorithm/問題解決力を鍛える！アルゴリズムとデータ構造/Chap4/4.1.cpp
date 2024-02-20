#include <iostream>
using namespace std;

int func(int N) {
  if (N == 0) return 0;
  else if (N == 1) return 0;
  else if (N == 2) return 1;

  return func(N - 1) + func(N - 2) + func(N - 3);
}

int main() {
  int N;
  cin >> N;
  cout << func(N) << endl;
}
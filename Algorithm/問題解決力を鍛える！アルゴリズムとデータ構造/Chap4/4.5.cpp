#include <iostream>
using namespace std;

void func(long long N, long long cur, int use, long long &counter) {
  if (cur > N) return;
  if (use == 0b111) counter++;

  func(N, cur * 10 + 7, use | 0b001, counter);

  func(N, cur * 10 + 5, use | 0b010, counter);

  func(N, cur * 10 + 3, use | 0b100, counter);
}

int main() {
  long long N;
  cin >> N;
  long long counter = 0;
  func(N, 0, 0, counter);
  cout << counter << endl;
}